from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from product.models import Category
from product.forms import CategoryForm
# Create your views here.


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    form_classes = CategoryForm
    template_name = "product/category_create.html"

    def get_success_url(self):
        return reverse('core:home')
