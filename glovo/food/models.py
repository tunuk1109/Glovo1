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
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store_image = models.ImageField(upload_to='store_images', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.store_name


class ContactInfo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
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


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class CarItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.cart}'


class ProductCombo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    combo_name = models.CharField(max_length=32)
    combo_image = models.ImageField(upload_to='combo_images')
    combo_price = DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.combo_name


class Burgers(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    burgers_image = models.ImageField(upload_to='burger_images')

    def __str__(self):
        return f'{self.product}'


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
    order_status = models.CharField(choices=STATUS_ORDER_CHOICES, max_length=16)
    product_combo = models.ForeignKey(ProductCombo, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier')
    STATUS_CHOICES = (
        ('available', 'available'),
        ('busy', 'busy')
    )
    status_courier = models.CharField(choices=STATUS_CHOICES, max_length=16, default='available')
    current_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_courier')

    def __str__(self):
        return f'{self.courier} - {self.status_courier}'


class ReviewStore(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.store} - {self.rating}'


class RatingCourier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.courier} - {self.stars}'
