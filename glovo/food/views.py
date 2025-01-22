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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    pagination_class = StorePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['store_name']
    ordering_fields = ['owner']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreOwnerListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner, CheckOwnerEdit]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreCreateAPIView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListOwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductListAPIVew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailAPIVew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

class ProductOwnerListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)

class ProductOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def get_queryset(self):
        return Product.objects.filter(store__owner=self.request.user)


class ProductComboListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['store']
    search_fields = ['combo_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductComboCreateAPIView(generics.CreateAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


class ProductComboOwnerListAPIView(generics.ListAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = StoreListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def get_queryset(self):
        return ProductCombo.objects.filter(store__owner=self.request.user)


class ProductComboOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSimpleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def get_queryset(self):
        return ProductCombo.objects.filter(store__owner=self.request.user)


class CartAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartItemListAPIView(generics.ListAPIView):
    queryset = CarItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CarItem.objects.filter(cart__user=self.request.user)

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner, CheckCourier]

class OrderOwnerAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderOwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner, CheckCourier]


class CourierListAPIView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckCourier, CheckOwner]

class CourierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckCourier, CheckOwner]


class ReviewStoreListAPIView(generics.ListAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewStoreCreateAPIView(generics.CreateAPIView):
    queryset = ReviewStore.objects.all()
    serializer_class = ReviewStoreSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckClient]

    def get_queryset(self):
        return ReviewStore.objects.filter(user=self.request.user)


class RatingCourierListAPIView(generics.ListAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingCourierDetailAPIView(generics.RetrieveAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingCourierCreateAPIView(generics.CreateAPIView):
    queryset = RatingCourier.objects.all()
    serializer_class = RatingCourierDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckClient]
    
