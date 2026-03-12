from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_dosen),
    path('<id>/approve/', views.approve_dosen),
    path('<id>/reject/', views.reject_dosen),
    path('<id>/delete/', views.delete_dosen),
    path('<id>/', views.detail_dosen),
]
