from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        loginData = LoginForm(request.POST)
        if loginData.is_valid():
            username = loginData.cleaned_data["username"].lower()
            password = loginData.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("landingpage:landingpage")
            else:
                loginData.add_error(None, "Invalid credentials")
                messages.error(request, "Invalid credentials")
        
    else:
        loginData = LoginForm()

    return render(request, "users/login.html", {
        "loginForm": loginData
    })

def logout_view(request):
    logout(request)
    return redirect("landingpage:landingpage")

def register(request):
    if request.user.is_authenticated:
        return redirect("landingpage:landingpage")
 
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data["username"].lower()
            email = registerForm.cleaned_data["email"]
            password = registerForm.cleaned_data["password"]

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect("landingpage:landingpage")
            except IntegrityError:
                registerForm.add_error("username", "Username taken")

    else:
        registerForm = RegisterForm()

    
    return render(request, "users/register.html", {
        "registerForm": registerForm
    })