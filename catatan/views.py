from . import models, forms
from django.shortcuts import render, redirect
from django.db.models.functions import ExtractWeekDay
from django.forms.models import model_to_dict
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from mahasiswa.models import Pkl



@login_required(login_url='/accounts/')
def index(req):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        # Check approval before allowing POST
        pkl = Pkl.objects.filter(owner=req.user).first()
        if not pkl or not pkl.approve or not pkl.approve2:
            messages.error(req, "PKL Anda belum disetujui sepenuhnya.")
            return redirect('/catatan/')
        
        judul = req.POST.get('judul')
        ket = req.POST.get('ket')
        selang = req.POST.get('selang')
        
        if judul and ket and selang:
            catatan_obj = models.Catatan.objects.create(
                owner=req.user,
                judul=judul,
                ket=ket,
                selang=selang
            )
            files = req.FILES.getlist('upload_img')
            for file in files:
                models.Gambar.objects.create(upload_img=file, catatan=catatan_obj)
            messages.success(req, "Catatan harian berhasil disimpan.")
        else:
            messages.error(req, "Gagal menyimpan. Pastikan semua field terisi.")
        return redirect('/catatan/')

    tasks = models.Catatan.objects.filter(owner=req.user).order_by('-waktu')

    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all().order_by('-waktu')
        
    # Get user's PKL to check status
    pkl = Pkl.objects.filter(owner=req.user).first()
    
    return render(req, 'catatan/index.html',{
        'data': tasks,
        'form_catatan': form_catatan,
        'form_gambar': form_gambar,
        'active_page': 'logbook',
        'pkl': pkl,
    })
    
@login_required(login_url='/accounts/')
def detail(req, id):
    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/detail.html', {
        'data': task,
    })
    
@login_required(login_url='/accounts/')
def delete(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/catatan/')

@login_required(login_url='/accounts/')
def index_dosen(req):
    group = req.user.groups.first()
    
    # By default fetch logbooks of students where req.user is the dosen
    pkls_dosen = Pkl.objects.filter(nama_dosen=req.user)
    mahasiswa_users = pkls_dosen.values_list('owner', flat=True)
    tasks = models.Catatan.objects.filter(owner__in=mahasiswa_users).order_by('-waktu')
    
    if group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all().order_by('-waktu')

    return render(req, 'catatan.d/index.html',{
        'data': tasks,
        'active_page': 'logbook'
    })

@login_required(login_url='/accounts/')
def evaluate_logbook(req, id):
    if req.method == 'POST':
        status = req.POST.get('status')
        if status in ['pending', 'acc', 'tolak']:
            catatan = models.Catatan.objects.filter(pk=id).first()
            if catatan:
                catatan.status = status
                catatan.save()
    return redirect('/catatan.d/')

@login_required(login_url='/accounts/')
def detail_dosen(req):

    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        catatans = models.Catatan.objects.filter(owner=req.user)
    return render(req, 'dosenah/index.html',{
        'data': catatans,
    })

# class list(ListView):
#     model = Catatan
#     template_name = 'catatan/index.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['get_percentage_done'] = models.Catatan.objects.filter(status = True, owner=req.user).first().count() * 100 / Task.objects.all().count()
#         return context

@login_required(login_url='/accounts/')
def new(req, *args, **kwargs):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            catatan_obj = form_catatan.save()
            files = req.FILES.getlist('upload_img')
            for file in files:
                models.Gambar.objects.create(upload_img=file, catatan=catatan_obj)
        return redirect('/catatan/')
    return render(req, 'catatan.d/index.html',{
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,
    })
