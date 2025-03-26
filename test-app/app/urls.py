from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView, CartView
from .views import AddToCartView, UpdateCartItemView, RemoveFromCartView, ClearCartView, CustomObtainTokenView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = 'API',
        default_version = 'v1',
        description="Тестовое задание по интернет-магазину",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list' ),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/update/<int:item_id>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('cart/clear/', ClearCartView.as_view(), name='clear-cart'),
    path('api-token-auth', CustomObtainTokenView.as_view(), name='api-token-auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
