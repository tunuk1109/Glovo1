from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users_list'),
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
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('product/', ProductListAPIVew.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIVew.as_view(), name='product_detail'),

]
