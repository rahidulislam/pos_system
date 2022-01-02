from django.urls import path

from purchase.views import PurchaseCreateView, PurchaseProductList

app_name = 'purchase'

urlpatterns = [
    path('create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('products/', PurchaseProductList.as_view(), name='purchase-product-list'),
]
