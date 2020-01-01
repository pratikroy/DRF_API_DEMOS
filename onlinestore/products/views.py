from django.shortcuts import render
#from django.views.generic import ListView, DetailView
from django.http import JsonResponse

from products.models import Manufacturer, Product

# Create your views here.
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }
        }, status=404)

    return response


def manufacturer_list(request):
    """return list of all active manufacturer"""
    manu_list = Manufacturer.objects.filter(is_active=True)
    data = {"manufacturers": list(manu_list.values())}
    res = JsonResponse(data)
    return res

def manufacturer_detail(request, pk):
    """return details of a manufacturer"""
    try:
        detail = Manufacturer.objects.get(pk=pk)
        manu_products = detail.products.all()
        data = {"manufacturer": {
            "name": detail.name,
            "location": detail.location,
            "is_active": detail.is_active,
            "product_detail": list(manu_products.values())
        }}
        res = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        res = JsonResponse({
            "error": {
                "code": "404",
                "message": "Manufacturer detail does not exist",
            }
        }, status=404)

    return res
