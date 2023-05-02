from django.shortcuts import get_object_or_404, redirect, render
from .models import Product

from django.urls import path, include
from . import views

urlpatterns = [
    path('catalog/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('delete/confirm/<pk>/', views.delete_confirm, name='delete_confirm'),
]