from django.db import models
from django.contrib.auth.models import User

class Dosen(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Dosen_profile', null=True, blank=True)
    nama_dosen = models.CharField(max_length=100)
    nip = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama_dosen    