from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.urls import reverse
from sell.forms import SellForm
from sell.models import Sell


class SellCreateView(CreateView):
    model = Sell
    form_class = SellForm
    template_name = 'sell/sell_create.html'

    def get_success_url(self):
        messages.success(self.request, '{} is created successfully'.format(self.object))
        return reverse('sell:sell-list')


class SellListView(ListView):
    model = Sell
    template_name = 'sell/sell_list.html'
    context_object_name = 'sells'


class SellUpdateView(UpdateView):
    model = Sell
    form_class = SellForm
    template_name = 'sell/sell_update.html'

    def get_success_url(self):
        messages.success(self.request, '{} is updated successfully'.format(self.object))
        return reverse('sell:sell-list')


class SellDetailVIew(DetailView):
    model = Sell
    template_name = 'sell/sell_detail.html'
    context_object_name = 'sell'


class SellDeleteView(DeleteView):
    model = Sell
    template_name = 'sell/sell_delete.html'
    context_object_name = 'sell'

    def get_success_url(self):
        messages.success(self.request, '{} is deleted successfully'.format(self.object))
        return reverse('sell:sell-list')
