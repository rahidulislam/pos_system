from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Biller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sell(models.Model):
    TAX_TYPE = (
        ('No Tax', 'No Tax'),
        ('GST@5%', 'GST@5%'),
        ('VAT%10%', 'VAT@10%')
    )
    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Due', 'Due'),
        ('Paid', 'Paid')
    )
    SALE_STATUS = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )
    reference_no = models.CharField("Reference No", max_length=100)
    biller = models.ForeignKey(Biller, on_delete=models.SET_NULL, blank=True, null=True, related_name='sell_biller')
    customer_name = models.CharField("Customer Name", max_length=100)
    sell_date = models.DateField()
    order_tax = models.CharField("Order TAX", max_length=50, choices=TAX_TYPE, default='No Tax')
    order_discount = models.PositiveIntegerField("Order Discount", default=0,
                                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    shipping = models.PositiveIntegerField(default=0)
    attachment = models.FileField(upload_to="sell", blank=True)
    sell_status = models.CharField("Sell Status", max_length=50, choices=SALE_STATUS, default='Pending')
    payment_status = models.CharField("Payment Status", max_length=50, choices=PAYMENT_STATUS, default='Pending')
    sell_note = models.TextField("", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reference_no

    def get_absolute_url(self):
        return reverse('sell:sell-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('sell:sell-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('sell:sell-delete', kwargs={'pk': self.pk})
