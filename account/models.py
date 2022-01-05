from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


# Create your models here.
class Profile(models.Model):
    GENDER_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE, default='Male')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


