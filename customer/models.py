from django.db import models
from django.urls import reverse


# Create your models here.

class CustomerGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Bangladesh")
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer:customer-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('customer:customer-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('customer:customer-delete', kwargs={'pk': self.pk})
