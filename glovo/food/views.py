from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from .paginations import StorePagination


class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    pagination_class = StorePagination


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class StoreOwnerListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreCreateAPIView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer


class CartAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer


class CartDetailAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer


class ProductListAPIVew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIVew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer


class ProductOwnerListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)

class ProductOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)


class ProductComboListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer


class ProductComboCreateAPIView(generics.CreateAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductSimpleSerializer


class ProductComboOwnerListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        return ProductCombo.objects.filter(store__owner=self.request.user)


class ProductComboOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSimpleSerializers


class CartItemListAPIView(generics.ListAPIView):
    queryset = CarItem.objects.all()
    serializer_class = CartItemListSerializer


class CartItemDetailAPIView(generics.RetrieveAPIView):
    queryset = CarItem.objects.all()
    serializer_class = CartItemDetailSerializer


class BurgersViewSet(viewsets.ModelViewSet):
    queryset = Burgers.objects.all()
    serializer_class = BurgersSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class ReviewStoreListAPIView(generics.ListAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSerializer


class ReviewStoreCreateAPIView(generics.CreateAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSimpleSerializer


class RatingCourierViewSet(viewsets.ModelViewSet):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierSerializer
    
