from django.db import models
from products.models import Product
from django.db.models.signals import post_save

"""Create model of Order"""


class Status(models.Model):
    name = models.CharField(max_length=12, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Status: %s" % self.name

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Status order"
        verbose_name_plural = "Statuses order"


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)  # total price for all products in order
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=12, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=256, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Order: %s %s" % (self.id, self.status.name)

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    nmb = models.IntegerField(default=1)
    """max_digits-number of characters, decimal_places-number of characters after','"""
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*number
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Product: %s" % self.product.name

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Product in order"
        verbose_name_plural = "Products in order"

    def save(self, *args, **kwargs):
        """calculate the total price"""
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item
        super(ProductsInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    """calculate the total cost of the order"""
    order = instance.order
    all_product_in_order = ProductsInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_product_in_order:
        order_total_price += item.total_price
        instance.order.total_price = order_total_price
        instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductsInOrder)  # Call the method 'post_save' to save the price
