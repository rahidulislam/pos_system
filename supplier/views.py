from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.urls import reverse
from supplier.models import Supplier
from supplier.forms import SupplierForm


# Create your views here.
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_create.html'

    def get_success_url(self):
        messages.success(self.request, "{0} is created successfully".format(self.object))
        return reverse("supplier:supplier-list")


class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_update.html'

    def get_success_url(self):
        messages.success(self.request, "{0} is updated successfully".format(self.object))
        return reverse("supplier:supplier-list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier/supplier_delete.html'
    context_object_name = 'supplier'

    def get_success_url(self):
        messages.success(self.request, "{0} is deleted successfully".format(self.object))
        return reverse("supplier:supplier-list")


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier/supplier_detail.html'
    context_object_name = 'supplier'
