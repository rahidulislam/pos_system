from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
