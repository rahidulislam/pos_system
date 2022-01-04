from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse
from django.contrib import messages
from customer.models import Customer
from customer.forms import CustomerForm


# Create your views here.
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_create.html'

    def get_success_url(self):
        messages.success(self.request, '{} is created successfully'.format(self.object))
        return reverse('customer:customer-list')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_update.html'

    def get_success_url(self):
        messages.success(self.request, '{} is updated successfully'.format(self.object))
        return reverse('customer:customer-list')


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'customer'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    context_object_name = 'customer'

    def get_success_url(self):
        messages.success(self.request, '{} is deleted successfully'.format(self.object))
        return reverse('customer:customer-list')
