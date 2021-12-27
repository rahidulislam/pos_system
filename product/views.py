from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from product.models import Category
from product.forms import CategoryForm
from django.contrib import messages


# Create your views here.


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'product/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ('parent', 'name', 'short_description', 'code', 'image', 'is_active')
    form_classes = CategoryForm
    template_name = "product/category_create.html"

    def get_success_url(self):
        messages.success(self.request, "Category is created successfully")
        return reverse('product:category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('parent', 'name', 'short_description', 'code', 'image', 'is_active')
    form_classes = CategoryForm
    template_name = "product/category_update.html"

    def get_success_url(self):
        messages.success(self.request, "Category is Updated successfully")
        return reverse('product:category-list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'
    context_object_name = 'category'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/category_delete.html'
    context_object_name = 'category'

    def get_success_url(self):
        messages.success(self.request, "Category is deleted successfully")
        return reverse('product:category-list')
