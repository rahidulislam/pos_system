from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, UpdateView, DetailView, DeleteView, RedirectView
from django.contrib.auth.forms import UserCreationForm
from account.forms import ProfileForm, UpdateUserForm, LoginForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
from account.models import Profile


class UserCreateView(View):
    template_name = 'account/user_create.html'

    def get(self, request):
        form = UserCreationForm
        profile_form = ProfileForm
        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, '{} is created Successfully'.format(user))
            return redirect('account:user-list')
        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})


class UserListView(ListView):
    model = User
    template_name = 'account/user_list.html'
    context_object_name = 'users'
    queryset = User.objects.filter(is_superuser=False).prefetch_related('profile')


class UserUpdateView(View):
    template_name = 'account/user_update.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UpdateUserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UpdateUserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user.profile)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, '{} is updated Successfully'.format(user))
            return redirect('account:user-list')
        return render(request, self.template_name, {'form': form, 'profile_form': profile_form})


class UserDetailView(DetailView):
    model = User
    template_name = 'account/user_detail.html'
    context_object_name = 'user'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'account/user_delete.html'

    def get_success_url(self):
        messages.success(self.request, '{} is deleted successfully'.format(self.object))
        return reverse('account:user-list')


class LoginView(View):
    template_name = 'account/login.html'
    from_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')
        form = self.from_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')

        form = self.from_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome {}, You are logged in Successfully'.format(user))
                return redirect('core:home')
        return render(request, self.template_name, {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('account:user-login')
