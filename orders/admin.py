from django.contrib import admin
from .models import *


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder
    extra = 1


class StatusAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in Status._meta.fields]  # displays all fields in model

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in Order._meta.fields]  # displays all fields in model
    inlines = [ProductsInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductsInOrderAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    list_display = [field.name for field in ProductsInOrder._meta.fields]  # displays all fields in model

    class Meta:
        model = ProductsInOrder


admin.site.register(ProductsInOrder, ProductsInOrderAdmin)
