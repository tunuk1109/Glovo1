from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import DecimalField
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(75)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    STATUS_CHOICES = (
        ('client', 'client'),
        ('courier', 'courier'),
        ('owner', 'owner'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=32, default='client')
    user_image = models.ImageField(upload_to='user_images', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.status}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_store')
    store_image = models.ImageField(upload_to='store_images', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.store_name} - {self.owner}'

    def get_avg_rating(self):
        rating = self.store_rating.all()
        if rating.exists():
            return round(sum([i.rating for i in rating]) / rating.count(), 1)

    def get_count_people(self):
        comment = self.store_rating.all()
        if comment.exists():
            return comment.count()
        return 0

class ContactInfo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact')
    title = models.CharField(max_length=32)
    phone_numbers = PhoneNumberField()
    social_network = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.store}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.cart_cart_item.all())
        return total_price


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_image = models.ImageField(upload_to='product_images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class CarItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.cart}'

    def get_total_price(self):
        return self.product.price * self.quantity


class ProductCombo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combo')
    combo_name = models.CharField(max_length=32)
    combo_image = models.ImageField(upload_to='combo_images', null=True, blank=True)
    combo_price = DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.combo_name}'


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='order_courier')
    STATUS_ORDER_CHOICES = (
        ('waiting', 'waiting'),
        ('process', 'process'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_combo = models.ForeignKey(ProductCombo, on_delete=models.CASCADE, null=True, blank=True)
    order_status = models.CharField(choices=STATUS_ORDER_CHOICES, max_length=16)
    delivery_address = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.courier}, {self.client}, {self.product}, {self.product_combo}'


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier')
    STATUS_CHOICES = (
        ('available', 'available'),
        ('busy', 'busy')
    )
    status_courier = models.CharField(choices=STATUS_CHOICES, max_length=16, default='available')
    current_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='order_courier')

    def __str__(self):
        return f'{self.courier} - {self.status_courier}'


class ReviewStore(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_rating')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.store} - {self.rating}'


class RatingCourier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_rating')
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                               null=True, blank=True, related_name='client_for_rating')

    def __str__(self):
        return f'{self.client} - {self.courier} - {self.stars}'
