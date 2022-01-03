from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from purchase.forms import PurchaseForm
from purchase.models import Purchase
from product.models import Product
from django.contrib import messages


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/purchase_create.html'

    def get_success_url(self):
        messages.success(self.request, '{0} is created successfully'.format(self.object))
        return reverse('purchase:purchase-list')


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase/purchase_list.html'
    context_object_name = 'purchases'


class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/purchase_update.html'

    def get_success_url(self):
        messages.success(self.request, '{} is updated successfully'.format(self.object))
        return reverse('purchase:purchase-list')



class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase/purchase_detail.html'
class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'purchase/purchase_delete.html'
    context_object_name = 'purchase'

    def get_success_url(self):
        messages.success(self.request, '{} is deleted successfully'.format(self.object))
        return reverse('purchase:purchase-list')
