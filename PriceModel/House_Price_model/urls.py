"""
URL configuration for PriceModel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from House_Price_model import views


urlpatterns = [
    path("admin/", admin.site.urls,name="admin"),
    path("", views.index, name="index"),
    path("login/", views.log_in, name="log_in"),
    path("register/", views.register, name="signin"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout/", views.log_out, name="log_out"),
    path("Price/", views.Price_Field, name="Price"),




]
