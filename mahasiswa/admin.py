from django.contrib import admin
from .models import Pkl

@admin.register(Pkl)
class PklAdmin(admin.ModelAdmin):
    list_display = ('judul', 'owner', 'nama_mitra', 'nama_dosen', 'approve', 'approve2')
    list_filter = ('approve', 'approve2', 'reject', 'reject2')
    search_fields = ('judul', 'owner__username')
