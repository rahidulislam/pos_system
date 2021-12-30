from django.urls import path
from supplier.views import SupplierCreateView,SupplierListView,SupplierUpdateView,SupplierDeleteView,SupplierDetailView

app_name = 'supplier'

urlpatterns = [
    path('', SupplierListView.as_view(), name="supplier-list"),
    path('create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier-delete'),
    path('detail/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail')
]
