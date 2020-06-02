from django.contrib import admin
from . models import *


class SubscriberAdmin(admin.ModelAdmin):
    """Sets the display options for the fields in the admin panel"""
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields] #displays all fields in model
    list_filter = ['name'] # create a filtel by fields
    search_fields = ['name', 'email'] # create search by fields
    fields = ["email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
