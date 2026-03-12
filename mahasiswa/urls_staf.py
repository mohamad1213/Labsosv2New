from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_staf),
    path('<id>/delete/', views.delete_staf),
    # path('<id>/update/', views.update_staf),
    path('<id>/approve/', views.approve),
    path('<id>/reject/',views.reject),
    path('<id>/detail/', views.detail_staf),
]
