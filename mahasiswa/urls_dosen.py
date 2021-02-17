from django.urls import path
from mahasiswa.views import ListView

from . import views

urlpatterns = [
    path('', views.index_dosen),
    path('<id>/', views.detail_dosen),
]
