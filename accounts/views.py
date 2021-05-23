from django.shortcuts import render,redirect
from .models import Account
from .forms import RegForm
from .forms import LoginForm
from django.contrib.auth import login,authenticate

# Create your views here.

def landpage(request):
    return render(request, 'acc-temp/landpage.html')

def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request,account)
            return redirect('accounts:landpage')
        return render(request, 'acc-temp/signup.html', {'SignupForm':form})
    else:
        form = RegForm(request.POST)
    return render(request, 'acc-temp/signup.html', {'SignupForm':form})


def LogIn(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request,account)
            return redirect('accounts:landpage')
        return render(request, 'acc-temp/login.html', {'LoginForm':form})
    else:
        form = LoginForm(request.POST)
    return render(request, 'acc-temp/login.html', {'LoginForm':form})


def useraccount(request):
    return render(request, 'acc-temp/useraccount.html')