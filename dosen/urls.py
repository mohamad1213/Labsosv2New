from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index),
    path('catatan/',views.catatan),
]
