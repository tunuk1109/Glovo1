from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'store', 'product_name', 'product_image', 'price', 'description']


class ProductComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCombo
        fields = '__all__'


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
    class Meta:
        model = ReviewStore
        fields = '__all__'


class RatingCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingCourier
        fields = '__all__'


class StoreListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category']

class StoreDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    category = CategoryListSerializer()
    combo = ProductComboSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['store_image', 'store_name', 'description', 'combo', 'address', 'category', 'owner',]


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_store = StoreListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_store']
