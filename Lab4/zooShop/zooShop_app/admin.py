from django.contrib import admin
from .models import Product, ProductType, Provider, Client

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['vendor_code', 'amount', 'name', 'description', 'cost', 'product_type', 'provider']
    list_filter = ['cost', 'product_type']

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['designation']

@admin.register(Provider)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth','email', 'phone_number' ]
    list_filter = ['first_name', 'last_name', 'date_of_birth','email', 'phone_number' ]
