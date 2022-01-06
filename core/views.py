from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product


# Create your views here.

class HomeView(LoginRequiredMixin, View):
    template_name = 'core/index.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})
