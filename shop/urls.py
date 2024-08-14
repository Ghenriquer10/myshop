from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop_index"),
    path("login/", views.userLogin, name="login"),
    path("register/", views.userRegister, name="register"),
]
