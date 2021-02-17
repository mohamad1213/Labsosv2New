from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Username..' })
		self.fields['email'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Email..' })
		self.fields['first_name'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Firstname..' })
		self.fields['last_name'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Lastname..' })
		self.fields['password1'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Enter Password..','id':'myInput'})
		self.fields['password2'].widget.attrs.update({ 'class': 'input100', 'placeholder': 'Re-enter Password..' })


