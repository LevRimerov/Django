from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Product: %s" % self.name

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Category of product"
        verbose_name_plural = "Category of products"


class Product(models.Model):
    """Create model of Product"""
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete = models.DO_NOTHING)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Product: %s" % self.name

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImages(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "Product: %s" % self.id

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
