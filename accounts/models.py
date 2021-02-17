from django.db import models
from django.contrib.auth.models import User
from dosen.models import Dosen
from forum.models import Forum


class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	owner = models.ForeignKey(User, default='',on_delete = models.DO_NOTHING,related_name='update')
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name
