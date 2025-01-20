from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'burgers', BurgersViewSet, basename='burgers_list'),
router.register(r'order', OrderViewSet, basename='order_list'),
router.register(r'courier', CourierViewSet, basename='courier_list'),
router.register(r'ratingCourier', RatingCourierViewSet, basename='ratingCourier_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='users_detail'),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store_list/', StoreOwnerListAPIView.as_view(), name='store_owner_list'),
    path('store_list/<int:pk>/', StoreOwnerEditAPIView.as_view(), name='store_owner_edit'),
    path('store_create/', StoreCreateAPIView.as_view(), name='store_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('product/', ProductListAPIVew.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIVew.as_view(), name='product_detail'),
    path('product_create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product_list/', ProductOwnerListAPIView.as_view(), name='product_owner_list'),
    path('product_list/<int:pk>/', ProductOwnerEditAPIView.as_view(), name='product_owner_detail'),
    path('combo_list/', ProductComboListAPIView.as_view(), name='combo_list'),
    path('combo_create/', ProductComboCreateAPIView.as_view(), name='combo_create'),
    path('combo_owner_list/', ProductOwnerListAPIView.as_view(), name='combo_owner_list'),
    path('combo_owner/<int:pk>/', ProductComboOwnerEditAPIView.as_view(), name='combo_owner_detail'),
    path('cart/', CartAPIView.as_view(), name='cart_list'),
    path('cart/<int:pk>/', CartDetailAPIView.as_view(), name='cart_detail'),
    path('cart_item/', CartItemListAPIView.as_view(), name='cart_item_list'),
    path('cart_item/<int:pk>/', CartItemDetailAPIView.as_view(), name='cart_item_detail'),
    path('review/', ReviewStoreListAPIView.as_view(), name='review_list'),
    path('review_create/', ReviewStoreCreateAPIView.as_view(), name='review_create')



]
