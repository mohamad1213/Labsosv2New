from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from . import models, forms
from dosen import models as dosen_models
from catatan.models import Catatan
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/')
def index(req):

    tasks_approved = models.Pkl.objects.filter(owner=req.user,approve=True).first()
    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()
    tasks2 = models.Forum.objects.all()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/mahasiswa')
        else:
            messages.error(req, 'A problem has been occurred while submitting your data.')
    return render(req, 'mahasiswa/index.html',{
        'form' : form_input,
        'data': tasks,
        'data2':tasks2,
        'data_approved': tasks_approved,
        
    })
    

@login_required(login_url='/accounts/')
def index_staf(req):
    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()
    form_reject = forms.RejectForm()
    
    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
        return redirect('/mahasiswas')
        

    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswas/index.html',{
        'data': tasks,
        'form_reject':form_reject,  
    })


class list(ListView):
    model = Catatan
    template_name = 'dosenah/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['get_percentage_done'] = Catatan.objects.filter(status = True).count() * 100 / Catatan.objects.all().count()
        return context

@login_required(login_url='/accounts/')
def index_dosen(req):
    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()
    form_reject = forms.RejectForm()
    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
        return redirect('/dosenah')
    group = req.user.groups.first() #mengambil group user
    tasks = models.Pkl.objects.all() # mengambil semua object yang ada di models pkl
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        pkls = models.Pkl.objects.filter(nama_dosen=req.user) # memfilter bahwa satu mahasiswa hanya boleh menginputkan satu dosen
    return render(req, 'dosenah/index.html',{
        'data': pkls,
        'form_reject':form_reject
    })

@login_required(login_url='/accounts/')
def detail_dosen(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=pkl.owner) # mengambil semua object yang ada di models Catatan
    
    return render(req, 'dosenah/detail.html',{
        'data': catatans,
    })

@login_required(login_url='/accounts/')
def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

@login_required(login_url='/accounts/')
def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/mahasiswa')

@login_required(login_url='/accounts/')
def delete_staf(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/mahasiswas')


@login_required(login_url='/accounts/')
def update(req, id):
    tasks_approved = models.Pkl.objects.filter(owner=req.user,approve=True).first()
    tasks = models.Pkl.objects.filter(owner=req.user)
    widgets = {
        'tanggal_mulai': DatePickerInput(),
        'tanggal_selesai': DatePickerInput(),
    }
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(
            judul=req.POST['judul'], 
            nama_dosen=req.POST['nama_dosen'], 
            tanggal_mulai=req.POST['tanggal_mulai'], 
            tanggal_selesai=req.POST['tanggal_selesai'])
        messages.info(req, 'data telah di perbarui.')
        return redirect('/mahasiswa')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/index.html', {
        'data': pkl,
        'data_approved': tasks_approved,

    })

@login_required(login_url='/accounts/')
def update_staf(req, id):
    widgets = {
        'tanggal_mulai': DatePickerInput(),
        'tanggal_selesai': DatePickerInput(),
    }
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(
            judul=req.POST['judul'], 
            nama_dosen=req.POST['nama_dosen'], 
            tanggal_mulai=req.POST['tanggal_mulai'], 
            tanggal_selesai=req.POST['tanggal_selesai'])
        return redirect('/mahasiswas')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswas/update.html', {
        'data': pkl,
    })

@login_required(login_url='/accounts/')
def approve(req, id):
    a = models.Pkl.objects.filter(pk=id).update(approve=True)
    return redirect('/mahasiswas')


@login_required(login_url='/accounts/')
def reject(req,id):
    form_reject = forms.RejectForm(req.POST)
    if req.POST:
        form_reject = forms.RejectForm(req.POST)
        if form_reject.is_valid():
            models.Pkl.objects.filter(pk=id).update(approve=False, reject=True, catatan=form_reject.cleaned_data['catatan'])

    return redirect('/mahasiswas')
