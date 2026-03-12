from django.contrib import admin
from .models import Dosen

@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
    list_display = ('nama_dosen', 'nip', 'fakultas', 'jurusan', 'owner')
    search_fields = ('nama_dosen', 'nip')
