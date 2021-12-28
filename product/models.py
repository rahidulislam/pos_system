from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name="Parent Category", on_delete=models.SET_NULL, blank=True,
                               null=True)
    name = models.CharField("Category Name", max_length=100, unique=True)
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


class Product(models.Model):
    PRODUCT_TYPE = (
        ('Standard', 'Standard'),
        ('Digital', 'Digital'),
        ('Service', 'Service')
    )
    TAX_METHOD = (
        ('Exclusive', 'Exclusive'),
        ('Inclusive', 'Inclusive')
    )
    name = models.CharField("Product Name", max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    code = models.CharField("Product Code", max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='product_category')
    type = models.CharField("Product Type", max_length=20, choices=PRODUCT_TYPE, default="Standard")
    cost = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)
    tax_method = models.CharField("Tax Method", max_length=20, choices=TAX_METHOD, default='Exclusive')
    description = models.TextField("Product Description", blank=True)
    image = models.ImageField(upload_to="product/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:product-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product:product-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('product:product-delete', kwargs={'slug': self.slug})

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
