from django.urls import path
from customer.views import CustomerCreateView,CustomerListView,CustomerUpdateView,CustomerDeleteView,CustomerDetail

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create/', CustomerCreateView.as_view(), name='customer-create'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('detail/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete')
]