from django.contrib import admin
from . models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductCategoryAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in ProductCategory._meta.fields] #displays all fields in model


    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in Product._meta.fields] #displays all fields in model
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in ProductImages._meta.fields] #displays all fields in model

    class Meta:
        model = ProductImages


admin.site.register(ProductImages, ProductImageAdmin)
