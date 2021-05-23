from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django.contrib.auth import authenticate

class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="a valid email address is required")
    first_name  = forms.CharField(max_length=30, help_text="required")
    last_name = forms.CharField(max_length=30, help_text="required")
    username = forms.CharField(max_length=30)
    class Meta:
        model = Account
        fields = ['email','first_name','last_name','username'] 

class LoginForm(forms.ModelForm):

    password = forms.CharField(label='password' )
    class Meta:
        model = Account
        fields = ['email','password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password'] 
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")