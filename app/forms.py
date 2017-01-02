from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile,Department


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('department',)
