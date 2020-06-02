from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        """Sets the parameters for displaying user data in the admin panel."""
        return "User: %s, Email: %s" % (self.name, self.email)

    class Meta:
        """Specifies the plural or singular"""
        verbose_name = "My subscriber"
        verbose_name_plural = "My subscribers"
