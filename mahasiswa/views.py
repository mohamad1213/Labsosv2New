from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from . import models, forms
from dosen import models as dosen_models
from catatan.models import Catatan
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


@login_required(login_url='/accounts/')
def index(req):
    tasks = models.Pkl.objects.filter(owner=req.user)
    # Cek apakah ada PKL yang sudah aktif (disetujui Staf & Dosen)
    pkl_is_active = tasks.filter(approve=True, approve2=True).exists()
    
    form_input = forms.PklForm()
    data_mitra = models.Forum.objects.all() # Asumsi ini data mitra (dari code sebelumnya)

    if req.method == 'POST':
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Pengajuan PKL berhasil dikirim.')
            return redirect('/mahasiswa/')
        else:
            messages.error(req, 'Gagal mengirim pengajuan. Periksa kembali form Anda.')
            
    dosen_group = Group.objects.filter(name='dosen').first()
    dosen_list = User.objects.filter(groups=dosen_group) if dosen_group else User.objects.none()
    
    return render(req, 'mahasiswa/index.html',{
        'form' : form_input,
        'data': tasks,
        'data2': data_mitra,
        'pkl_is_active': pkl_is_active,
        'dosen_list': dosen_list,
        'active_page': 'pkl',
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
        'active_page': 'pkl'
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
        'form_reject':form_reject,
        'active_page': 'mahasiswa'
    })

@login_required(login_url='/accounts/')
def detail_dosen(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=pkl.owner).order_by('-waktu')
    
    return render(req, 'dosenah/detail.html',{
        'data': catatans,
        'pkl': pkl,
    })

@login_required(login_url='/accounts/')
def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

@login_required(login_url='/accounts/')
def detail_staf(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()
    # Fetch other students at the same institution (mitra)
    other_students = models.Pkl.objects.filter(nama_mitra=pkl.nama_mitra).exclude(pk=id)
    catatans = Catatan.objects.filter(owner=pkl.owner)
    
    return render(req, 'mahasiswas/detail.html', {
        'data': pkl,
        'others': other_students,
        'catatans': catatans,
        'active_page': 'pkl'
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
        pkl_obj = models.Pkl.objects.get(pk=id)
        if 'judul' in req.POST:
            pkl_obj.judul = req.POST['judul']
        if 'tanggal_mulai' in req.POST:
            pkl_obj.tanggal_mulai = req.POST['tanggal_mulai']
        if 'tanggal_selesai' in req.POST:
            pkl_obj.tanggal_selesai = req.POST['tanggal_selesai']
        if 'proposal' in req.FILES:
            pkl_obj.proposal = req.FILES['proposal']
        pkl_obj.save()
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
def approve_dosen(req, id):
    models.Pkl.objects.filter(pk=id).update(approve2=True, reject2=False)
    messages.success(req, 'Data PKL telah disetujui oleh Dosen.')
    return redirect('/dosenah')

@login_required(login_url='/accounts/')
def reject_dosen(req, id):
    if req.POST:
        catatan = req.POST.get('catatan', '')
        models.Pkl.objects.filter(pk=id).update(approve2=False, reject2=True, catatan=catatan)
        messages.warning(req, 'Data PKL telah ditolak oleh Dosen.')
    return redirect('/dosenah')

@login_required(login_url='/accounts/')
def delete_dosen(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    messages.success(req, 'Data PKL telah dihapus.')
    return redirect('/dosenah')

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
