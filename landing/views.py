from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product, ProductImages


def landing(request):
    name = "Rimerov Lev"
    current_date = "28.04.2020"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        print(data["email"])
        new_form = form.save()
    return render(request, 'landing/../../templates/landing/landing.html', locals())


def home(request):
    products_images = ProductImages.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category=1)
    products_images_laptops = products_images.filter(product__category=2)
    return render(request, 'landing/home.html', locals())
