from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    
]
