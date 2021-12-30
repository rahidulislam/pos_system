from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, View
from product.models import Category, Product
from product.forms import CategoryForm, ProductFrom
from django.contrib import messages


# Create your views here.


class CategoryListView(ListView):
    """Category List"""
    model = Category
    context_object_name = 'categories'
    template_name = 'product/category_list.html'


class CategoryCreateView(CreateView):
    """Create New Category"""
    model = Category
    fields = ('parent', 'name', 'short_description', 'code', 'image', 'is_active')
    form_classes = CategoryForm
    template_name = "product/category_create.html"

    def get_success_url(self):
        messages.success(self.request, "{0} Category is created successfully".format(self.object))
        return reverse('product:category-list')


class CategoryUpdateView(UpdateView):
    """Update Existing Category"""
    model = Category
    fields = ('parent', 'name', 'short_description', 'code', 'image', 'is_active')
    form_classes = CategoryForm
    template_name = "product/category_update.html"

    def get_success_url(self):
        messages.success(self.request, "{0} Category is Updated successfully".format(self.object))
        return reverse('product:category-list')


class CategoryDetailView(DetailView):
    """Detail Existing Category"""
    model = Category
    template_name = 'product/category_detail.html'
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    """Delete Existing Category"""
    model = Category
    template_name = 'product/category_delete.html'
    context_object_name = 'category'

    def get_success_url(self):
        messages.success(self.request, "{0} Category is deleted successfully".format(self.object))
        return reverse('product:category-list')


class ProductCreateView(CreateView):
    """Create New Category"""
    model = Product
    form_classes = ProductFrom
    fields = ['name', 'code', 'category', 'type', 'cost', 'price', 'quantity', 'tax_method', 'description', 'image']
    template_name = 'product/product_create.html'

    def get_success_url(self):
        messages.success(self.request, "{0} product is created successfully".format(self.object))
        return reverse('product:product-list')


class ProductListView(ListView):
    """All Product List"""
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    """Update Existing Product"""
    model = Product
    form_classes = ProductFrom
    fields = ['name', 'code', 'category', 'type', 'cost', 'price', 'quantity', 'tax_method', 'description', 'image']
    template_name = 'product/product_update.html'

    def get_success_url(self):
        messages.success(self.request, "{0} product is updated successfully".format(self.object))
        return reverse('product:product-list')


class ProductDetailView(DetailView):
    """Detail Existing Product"""
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    """Delete Existing Product"""
    model = Product
    template_name = 'product/product_delete.html'
    context_object_name = 'product'

    def get_success_url(self):
        messages.success(self.request, "{0} Product is deleted successfully".format(self.object))
        return reverse('product:product-list')
