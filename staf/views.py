from django.shortcuts import render, redirect
from . import models, forms
from mahasiswa.models import Pkl
from mitra.models import Mitra


def mahasiswa(req):
    staf = models.Pkl.objects.all()
    return render(req, 'staf/index.html',{
        'data': staf,
    })

def mitra(req):
    staf = models.Mitra.objects.all()
    return render(req, 'staf/mitra.html',{
        'data': staf,
    })