from django.contrib import admin
from .models import Product


admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'image_url')
#     search_fields = ('name', 'description')


