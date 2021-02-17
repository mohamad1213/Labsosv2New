from django.db import models
from django.contrib.auth.models import User

class Mitra(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mitra')
    nama_mitra = models.CharField( max_length=255)
    alamat = models.CharField( max_length=255)
    deskripsi = models.TextField(default='')
    pic = models.CharField( max_length=255)
    telp = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_mitra

