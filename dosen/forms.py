from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

# Mapping Fakultas ke Program Studi UNU Yogyakarta
PRODI_CHOICES = [
    ('', '-- Pilih Program Studi --'),
    # Teknologi Informasi
    ('Informatika', 'Informatika'),
    ('Teknik Elektro', 'Teknik Elektro'),
    ('Teknik Komputer', 'Teknik Komputer'),
    # Ekonomi
    ('Manajemen', 'Manajemen'),
    ('Akuntansi', 'Akuntansi'),
    # Pendidikan
    ('Pendidikan Bahasa Inggris', 'Pendidikan Bahasa Inggris'),
    ('Pendidikan Guru Sekolah Dasar', 'Pendidikan Guru Sekolah Dasar'),
    # Dirasah Islamiyah
    ('Studi Islam Interdisipliner', 'Studi Islam Interdisipliner'),
    # Industri Halal
    ('Agribisnis', 'Agribisnis'),
    ('Farmasi', 'Farmasi'),
    ('Teknologi Hasil Pertanian', 'Teknologi Hasil Pertanian'),
]

FAKULTAS_CHOICES = [
    ('', '-- Pilih Fakultas --'),
    ('Fakultas Teknologi Informasi', 'Fakultas Teknologi Informasi'),
    ('Fakultas Ekonomi', 'Fakultas Ekonomi'),
    ('Fakultas Pendidikan', 'Fakultas Pendidikan'),
    ('Fakultas Dirasah Islamiyah', 'Fakultas Dirasah Islamiyah'),
    ('Fakultas Industri Halal', 'Fakultas Industri Halal'),
]

class DosenForm(ModelForm):
    fakultas = forms.ChoiceField(choices=FAKULTAS_CHOICES, widget=forms.Select(attrs={'class': 'fi', 'id': 'id_fakultas'}))
    jurusan = forms.ChoiceField(choices=PRODI_CHOICES, widget=forms.Select(attrs={'class': 'fi', 'id': 'id_jurusan'}))

    class Meta :
        model = models.Dosen
        exclude=['owner']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email']