from django.urls import path

from product.views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDetailView, \
    CategoryDeleteView, ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView,ProductDetailView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('update/<slug:slug>/', ProductUpdateView.as_view(), name='product-update'),
    path('delete/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
    path('detail/<slug:slug>/',ProductDetailView.as_view(), name='product-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/detail/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
]
