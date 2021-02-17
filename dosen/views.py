from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from mahasiswa.models import Pkl
from catatan.models import Catatan
from . import models, forms
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/')
def index(req):
    return render(req, 'dosen/index.html')

@login_required(login_url='/accounts/')
def detail_dosen(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=pkl.owner) # mengambil semua object yang ada di models Catatan
    return render(req, 'dosenah/detail.html',{
        'data': catatans,
    })
@login_required(login_url='/accounts/')
def detail_staf(req, id):
    dosen = models.Dosen.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=dosen.owner) # mengambil semua object yang ada di models Catatan
    return render(req, 'dosens/detail.html',{
        'data': catatans,
    })  

@login_required(login_url='/accounts/')
def index_staf(req):
    tasks = models.Dosen.objects.all()
    form_input = forms.DosenForm()
    form_user = forms.CreateUserForm()
    # group = Group.objects.get(name='dosen')


    if req.POST:
        form_input = forms.DosenForm(req.POST, req.FILES)
        form_user = forms.CreateUserForm(req.POST)
        if form_input.is_valid() or form_user.is_valid():
            form_input.instance.owner=req.user
            form_input.save()
            user = form_user.save()
            group = Group.objects.get(name='dosen') 
            user.groups.add(group)
            subject = 'Selamat Datang di SIM-Labsos'
            message = f'Hi dosen pembimbing Silahkan masuk akun dengan username = {user.username}, dan password = {user.password1} thank you for registering in SIM-Labsos'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [user.email,user.password1 ] 
            send_mail( subject, message, email_from, recipient_list ) 
            return redirect('/dosens/')

    return render(req, 'dosens/index.html',{
        'data': tasks,
        'form' : form_input,
        'form_user' : form_user,
    })

@login_required(login_url='/accounts/')
def catatan(req, id):
    dosen = models.Dosen.objects.all()

    group = req.user.groups.first(pk=id)
    if group is not None and group.name == 'dosen':
        mahasiswa = models.Pkl.objects.all()
    return render(req, 'dosen/catatan.html',{
        'data': dosen,
        'data': mahasiswa,
    })

@login_required(login_url='/accounts/')
def update_staf(req, id):
    if req.POST:
        mitra = models.Dosen.objects.filter(pk=id).update(nip=req.POST['nip'], nama_dosen=req.POST['nama_dosen'], fakultas=req.POST['fakultas'], jurusan=req.POST['jurusan'])
        return redirect('/dosens/')

    dosen = models.Dosen.objects.filter(pk=id).first()
    return render(req, 'dosens/update.html', {
        'data': dosen,
    })

@login_required(login_url='/accounts/')
def delete_staf(req, id):
    models.Dosen.objects.filter(pk=id).delete()
    return redirect('/dosens/')
