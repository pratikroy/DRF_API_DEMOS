from django.urls import path
#from products.views import ProductDetailView, ProductListView
from products.views import (product_list,
                            product_detail,
                            manufacturer_list,
                            manufacturer_detail)

urlpatterns = [
    path('products/', product_list, name="product-list"),
    path('products/<int:pk>/', product_detail, name='product-list'),
    path('manufacturers/', manufacturer_list, name='manu-list'),
    path('manufacturers/<int:pk>/', manufacturer_detail, name='manu-detail'),
]
