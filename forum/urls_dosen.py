from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index_dosen),
    path('<id>/', views.detail_forum_d),
    path('<id>/posting/<id_posting>/delete/', views.delete_posting_d),
    path('<id>/posting/<id_posting>/komen', views.dosen_komen),
    path('<id>/posting/<id_posting>/delete/komen', views.delete_komen_d),

]