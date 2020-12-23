"""ProyectoF1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('registrocliente/', views.registroCliente, name='registrocliente'),
    path('registroempresa/', views.registroEmpresa, name="registroempresa"),
    path('loginadmin/', views.loginAdmin, name="loginadmin"),
    path('logout/', views.logout, name="logout"),
    path('addCuentaMonetaria/', views.addCuentaMonetaria, name="addCuentaMonetaria"),
    path('addCuentaAhorro/', views.addCuentaDeAhorro, name="addCuentaAhorro"),
    path('addcuentaplazofijo/', views.addCuentaPlazoFijo, name="addCuentaPlazoFijo"),
]
