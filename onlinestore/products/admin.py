from django.contrib import admin
from products.models import Manufacturer, Product

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Product)
