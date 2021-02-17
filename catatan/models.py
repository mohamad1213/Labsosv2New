from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
import PIL.Image
import os

class Catatan(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='catatan')
    tgl_kegiatan = models.DateField(auto_now=True)
    waktu = models.DateTimeField(auto_now_add=True)
    now = datetime.now().replace(microsecond=0)
    judul = models.CharField(max_length=100)
    ket = models.TextField(max_length=500, help_text="maksimal 500 kata")
    selang = models.IntegerField(help_text="Dalam Menit")
    
class Gambar(models.Model):
    upload_img = models.FileField(default='', upload_to='images/', null=False, blank=True)
    catatan = models.ForeignKey(Catatan, on_delete=models.CASCADE, related_name='catatan')

    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        super(Gambar, self).save(*args, **kwargs)
        if self.upload_img and os.path.splitext(self.upload_img.name)[1] in ['.jpg', '.jpeg','.png']:
            upload_img = self.upload_img
            if upload_img.size > 0.3*1024*1024: #jika lebih dari 300kb maka akan otomatis terkompress
                self.compress_image(upload_img)
                print(upload_img)

    def compress_image(self, uploadedImage):
        im = PIL.Image.open("{}/{}".format(settings.MEDIA_ROOT,uploadedImage))
        if im.mode != 'RGB':
            im = im.convert('RGB')
        new_image = im.resize((round(im.size[0]*0.2), round(im.size[1]*0.2)))
        new_image.save('{}/{}'.format(settings.MEDIA_ROOT,uploadedImage))

    def upload_location(instance, filename, **kwargs):
        file_path = 'images/{filename}'.format(filename=filename)
        return file_path
   
    def __str__(self):
        return self.upload_img.url
