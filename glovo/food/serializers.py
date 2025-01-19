from rest_framework import serializers
from .models import *



class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'status']


class UserProfileClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['title', 'phone_numbers', 'social_network']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'store', 'product_name', 'product_image', 'price', 'description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'price', 'description']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    cart_cart_item = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'price', 'cart_cart_item', 'description']


class BurgersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burgers
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class ReviewStoreSerializer(serializers.ModelSerializer):
    client = UserProfileClientSerializer()
    created_date = serializers.DateField(format=('%d-%m-%Y'))

    class Meta:
        model = ReviewStore
        fields = ['client', 'comment', 'rating', 'created_date']


class RatingCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingCourier
        fields = '__all__'


class StoreSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name']


class StoreListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    store_rating = ReviewStoreSerializer(many=True, read_only=True)
    get_avg_rating = serializers.ModelSerializer()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category', 'store_rating', 'get_avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class StoreListOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_store = StoreListSerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['category_name', 'category_store']


class ProductComboSerializer(serializers.ModelSerializer):
    store = StoreSimpleSerializer()

    class Meta:
        model = ProductCombo
        fields = ['combo_name', 'combo_image', 'combo_price', 'description', 'store']


class StoreDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    category = CategoryListSerializer()
    combo = ProductComboSerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    contact = ContactInfoSerializer(many=True, read_only=True)
    store_rating = ReviewStoreSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['store_image', 'store_name', 'description', 'category', 'contact', 'product',
                  'combo', 'address', 'owner', 'store_rating']
