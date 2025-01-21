from rest_framework import viewsets, generics, permissions
from .models import *
from .serializers import *
from .paginations import StorePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from .permissions import CheckOwner, CheckOwnerEdit,CheckClient, CheckCourier



class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['store_name']
    ordering_fields = ['owner']
    permission_classes = [CheckClient]



class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [CheckClient]


class StoreOwnerListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer
    permission_classes = [CheckOwner, CheckOwnerEdit]


class StoreCreateAPIView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer
    permission_classes = [CheckOwner]


class ProductListAPIVew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailAPIVew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [CheckOwner]


class ProductOwnerListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)

class ProductOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)


class ProductComboListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['store']
    search_fields = ['combo_name']

class ProductComboCreateAPIView(generics.CreateAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [CheckOwner]


class ProductComboOwnerListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = StoreListSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return ProductCombo.objects.filter(store__owner=self.request.user)


class ProductComboOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSimpleSerializers
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)

    def get_queryset(self):
        return ProductCombo.objects.filter(store__owner=self.request.user)


class CartAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemListAPIView(generics.ListAPIView):
    queryset = CarItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CarItem.objects.filter(cart__user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderOwnerAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderOwnerSerializer


class CourierListAPIView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierListSerializer
    permission_classes = [CheckCourier]

class CourierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierDetailSerializer
    permission_classes = [CheckCourier]


class ReviewStoreListAPIView(generics.ListAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSerializer
    permission_classes = [CheckClient]


class ReviewStoreCreateAPIView(generics.CreateAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSimpleSerializer
    permission_classes = [CheckClient]

    def get_queryset(self):
        return ReviewStore.objects.filter(user=self.request.user)


class RatingCourierListAPIView(generics.ListAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierListSerializer
    permission_classes = [CheckClient]

class RatingCourierDetailAPIView(generics.RetrieveAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierDetailSerializer
    permission_classes = [CheckClient]

class RatingCourierCreateAPIView(generics.CreateAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierDetailSerializer
    permission_classes = [CheckClient]
    
