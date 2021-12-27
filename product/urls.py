from django.urls import path
from product.views import CategoryCreateView, CategoryListView,CategoryUpdateView,CategoryDetailView,CategoryDeleteView

app_name = 'product'

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/detail/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
]
