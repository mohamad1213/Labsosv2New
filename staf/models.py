from django.db import models

class Staf (models.Model):
    nim = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    