from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('', HomeView.as_view(), name='home'),
    # path('api/data/', get_data, name='api-data'),
    # path('api/chart/data/', ChartData.as_view()),
    path('cetak/', views.cetak),
    path('cetak_dosen/', views.cetak_dosen),
    path('cetak_staf/', views.cetak_staf),
    path('<id>/delete/', views.delete_catatan),
    path('<id>/delete/', views.delete_catatan),
]
