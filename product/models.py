from django.db import models

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=("Parent Category"), on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(("Category Name"), max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(("Category Code"), max_length=50)
    image = models.ImageField(("Category Image"), upload_to="category", blank=True)
    is_active = models.BooleanField(("Active"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name