from rest_framework import viewsets, generics
from .models import *
from .serializers import  *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductComboViewSet(viewsets.ModelViewSet):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer


class CarItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CarItemSerializer


class BurgersViewSet(viewsets.ModelViewSet):
    queryset = Burgers.objects.all()
    serializer_class = BurgersSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class ReviewStoreViewSet(viewsets.ModelViewSet):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSerializer


class RatingCourierViewSet(viewsets.ModelViewSet):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierSerializer
    
