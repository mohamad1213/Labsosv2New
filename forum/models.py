from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files import File
from django.conf import settings
import PIL.Image
import os


# Create your models here.

class Forum(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='forum')
    nama_mitra = models.CharField(max_length=255)
    alamat = models.CharField( max_length=255)
    deskripsi = models.TextField(default='')
    pic = models.CharField( max_length=255)
    telp = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_mitra

class Posting(models.Model):
    forum = models.ForeignKey(Forum, on_delete = models.DO_NOTHING,related_name='posting')
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='owner')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=200)
    upload_img = models.FileField(upload_to='images/', null=True, blank=True)
    class Meta :
        ordering = ['-waktu']
        
    @property
    def upload_img_url(self):
        if self.upload_img and hasattr(self.upload_img, 'url'):
            return self.upload_img.url
        return ''

    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        super(Posting, self).save(*args, **kwargs)
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
        return self.upload_img_url

    

class Komen(models.Model):
    posting = models.ForeignKey(Posting, on_delete = models.CASCADE,related_name='komentar')
    pengguna = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pengguna')
    waktu = models.DateTimeField(default=datetime.now)
    komentar = models.CharField(max_length=100)

class Balas(models.Model):
    komen = models.ForeignKey(Komen, on_delete = models.DO_NOTHING,related_name='balasan')
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='user')
    waktu = models.DateTimeField(default=datetime.now)
    balasan = models.TextField()


