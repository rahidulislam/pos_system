from django.db import models
from supplier.models import Supplier
from django.core.validators import MinValueValidator, MaxValueValidator
from product.models import Product


# Create your models here.
class Purchase(models.Model):
    RECEIVED_TYPE = (
        ('Received', 'Received'),
        ('Not Received', 'Not Received')
    )
    purchase_no = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchase_supplier')
    discount = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.purchase_no


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_product')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
