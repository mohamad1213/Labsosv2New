from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index_staf),
    path('<id>/update/', views.update_staf),
    path('<id>/', views.detail_forum),
    path('<id>/delete/', views.delete_forum),
    path('<id>/posting/<id_posting>/delete/', views.delete_posting),
    path('<id>/posting/<id_komen>/delete/komen', views.delete_komen),
    path('<id>/posting/<id_posting>/komen', views.staf_komen),
    path('<id>/komen/<id_posting>/delete/', views.delete_komen),
]