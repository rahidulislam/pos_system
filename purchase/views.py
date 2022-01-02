from django.shortcuts import render
from django.views.generic import CreateView,ListView

from purchase.forms import PurchaseForm
from purchase.models import Purchase
from product.models import Product


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/purchase_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class PurchaseProductList(ListView):
    model = Product
    template_name = 'purchase/purchase_item.html'
