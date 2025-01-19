from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'cart', CartViewSet, basename='cart_list'),
router.register(r'carItem', CartItemViewSet, basename='carItem_list'),
router.register(r'productCombo', ProductComboViewSet, basename='productCombo_list'),
router.register(r'burgers', BurgersViewSet, basename='burgers_list'),
router.register(r'order', OrderViewSet, basename='order_list'),
router.register(r'courier', CourierViewSet, basename='courier_list'),
router.register(r'reviewStore', ReviewStoreViewSet, basename='reviewStore_list'),
router.register(r'ratingCourier', RatingCourierViewSet, basename='ratingCourier_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store_list/', StoreOwnerListAPIView.as_view(), name='store_owner'),
    path('store_list/<int:pk>/', StoreOwnerEditAPIView.as_view(), name='store_owner_edit'),
    path('store_create/', StoreCreateAPIView.as_view(), name='store_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('product/', ProductListAPIVew.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIVew.as_view(), name='product_detail'),
    path('users/', UserProfileAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='users_detail'),

]
