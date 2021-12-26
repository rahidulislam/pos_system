from django.urls import path
from product.views import CategoryCreateView


app_name = 'product'

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
]
