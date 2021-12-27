from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name="Parent Category", on_delete=models.SET_NULL, blank=True,
                               null=True)
    name = models.CharField("Category Name", max_length=100)
    short_description = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(unique=True)
    code = models.CharField("Category Code", max_length=50)
    image = models.ImageField("Category Image", upload_to="category", blank=True)
    is_active = models.BooleanField("Active", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('product:category-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product:category-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product:category-delete', kwargs={'slug': self.slug})
