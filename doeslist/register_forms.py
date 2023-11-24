from django import forms
from .models import Custom_User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
import re



class User_Registration_Form(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', password1) or not re.search(r'\d', password1) or not re.search(r'[^A-Za-z0-9]', password1) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise ValidationError("Password must contain letters, numbers, and special characters.")
        return password1

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise ValidationError("Username must be at least 6 characters long.")
        return username

    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
        }
        labels = ['username', 'email', 'password1', 'password2']
