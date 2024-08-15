from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, CustomUserLoginForm


def userRegister(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def index(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserLoginForm()
    return render(request, "registration/index.html", {"form": form})


def home(request):
    user = request.user
    return render(request, "user/home.html", {"user": user})
