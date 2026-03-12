from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from forum.models import Forum
from dosen.models import Dosen

class Pkl(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswa')
    judul = models.CharField(max_length=255)
    proposal = models.FileField(upload_to='proposals/', blank=True, null=True)
    nama_mitra = models.ForeignKey(Forum, on_delete = models.DO_NOTHING)
    nama_dosen = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "dosen"}, on_delete = models.DO_NOTHING, related_name='membimbing')
    tanggal_mulai = models.DateField(default=datetime.now)
    tanggal_selesai = models.DateField()
    create_time = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    complete_time = models.DateTimeField(blank=True, null=True)
    approve = models.BooleanField(default=False)
    approve2 = models.BooleanField(default=False)
    catatan = models.TextField(max_length=1500, help_text="maksimal 1500 karakter")
    reject = models.BooleanField(default=False)
    reject2 = models.BooleanField(default=False)

    
    def __str__(self):
            return self.judul
    def tanggal_mulai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m-%d')
    def tanggal_selesai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m-%d')
    def range(self):
        return self.tanggal_selesai - datetime.now().date()
    def jatuhtempo(self):
        return self.range().days




