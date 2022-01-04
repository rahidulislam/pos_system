from django.urls import path
from sell.views import SellCreateView, SellListView, SellUpdateView, SellDeleteView, SellDetailVIew

app_name = 'sell'

urlpatterns = [
    path('', SellListView.as_view(), name='sell-list'),
    path('create/', SellCreateView.as_view(), name='sell-create'),
    path('update/<int:pk>/', SellUpdateView.as_view(), name='sell-update'),
    path('detail/<int:pk>/', SellDetailVIew.as_view(), name='sell-detail'),
    path('delete/<int:pk>/', SellDeleteView.as_view(), name='sell-delete'),
]
