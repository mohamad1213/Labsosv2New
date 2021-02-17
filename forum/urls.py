from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index_mhs),
    path('<id>/', views.detail_forum_mhs),
    path('<id>/posting/<id_posting>/delete/', views.delete_posting_mhs),
    path('<id>/posting/<id_posting>/komen/<id_komen>/delete', views.delete_komen_mhs),
    path('<id>/posting/<id_posting>/komen', views.mhs_komen),
]
