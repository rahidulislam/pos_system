from django.db import models
from django.urls import reverse


# Create your models here.
class Supplier(models.Model):
    name = models.CharField("Supplier Name", max_length=150)
    phone = models.CharField("Phone Number", max_length=50)
    phone2 = models.CharField("Another Phone Number", max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier:supplier-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('supplier:supplier-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('supplier:supplier-delete', kwargs={'pk': self.pk})
