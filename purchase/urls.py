from django.urls import path

from purchase.views import PurchaseCreateView, PurchaseListView, PurchaseUpdateView,PurchaseDeleteView,\
    PurchaseDetailView

app_name = 'purchase'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('update/<int:pk>/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('delete/<int:pk>/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('detail/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
]
