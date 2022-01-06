from django.urls import path
from account.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, UserDetailView, LoginView, LogOutView
app_name = 'account'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogOutView.as_view(), name='user-logout'),
]
