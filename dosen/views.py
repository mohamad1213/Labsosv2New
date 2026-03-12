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
from django.contrib import messages

@login_required(login_url='/accounts/')
def index(req):
    return render(req, 'dosen/index.html')

@login_required(login_url='/accounts/')
def detail_dosen(req, id):
    pkl = Pkl.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=pkl.owner)
    return render(req, 'dosenah/detail.html',{
        'data': catatans,
    })

@login_required(login_url='/accounts/')
def detail_staf(req, id):
    dosen = models.Dosen.objects.filter(pk=id).first()
    # Menghitung statistik bimbingan
    if dosen and dosen.owner:
        mahasiswa_bimbingan = Pkl.objects.filter(nama_dosen_id=dosen.owner.id)
    else:
        mahasiswa_bimbingan = Pkl.objects.none()
        
    total_mhs = mahasiswa_bimbingan.count()
    mhs_aktif = mahasiswa_bimbingan.filter(approve=True, approve2=True).count()
    mhs_pending = mahasiswa_bimbingan.filter(approve2=False, reject2=False).count()

    return render(req, 'dosens/detail.html',{
        'data': dosen,
        'mhs': mahasiswa_bimbingan,
        'stat': {
            'total': total_mhs,
            'aktif': mhs_aktif,
            'pending': mhs_pending
        },
        'active_page': 'dosen'
    })  

@login_required(login_url='/accounts/')
def index_staf(req):
    # Auto-sync: Pastikan semua User di group 'dosen' punya profil Dosen
    dosen_group = Group.objects.filter(name='dosen').first()
    if dosen_group:
        users_in_group = User.objects.filter(groups=dosen_group)
        for user in users_in_group:
            # Jika belum ada profil Dosen untuk user ini, buatkan
            if not models.Dosen.objects.filter(owner=user).exists():
                models.Dosen.objects.create(
                    owner=user,
                    nama_dosen=user.first_name if user.first_name else user.username,
                    nip='-',
                    fakultas='-',
                    jurusan='-'
                )

    tasks = models.Dosen.objects.all().order_by('nama_dosen')
    form_input = forms.DosenForm()
    form_user = forms.CreateUserForm()

    if req.POST:
        action = req.POST.get('action')
        if action == 'create':
            form_input = forms.DosenForm(req.POST, req.FILES)
            form_user = forms.CreateUserForm(req.POST)
            if form_input.is_valid() and form_user.is_valid():
                user = form_user.save()
                
                # Link User ke Dosen profile
                dosen_profile = form_input.save(commit=False)
                dosen_profile.owner = user
                dosen_profile.save()
                
                # Add to Group Dosen
                try:
                    group, created = Group.objects.get_or_create(name='dosen')
                    user.groups.add(group)
                except:
                    pass
                
                raw_password = req.POST.get('password1', '**********')
                subject = 'Akun Dosen SIM-Labsos Baru'
                message = f'Halo Bpk/Ibu {dosen_profile.nama_dosen},\n\nAkun Anda telah dibuat oleh Admin.\nUsername: {user.username}\nPassword: {raw_password}\n\nSilakan login di SIM-Labsos.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [user.email] 
                try:
                    send_mail(subject, message, email_from, recipient_list)
                except:
                    pass
                
                messages.success(req, f'Dosen {dosen_profile.nama_dosen} berhasil ditambahkan.')
                return redirect('/dosens/')
            else:
                messages.error(req, 'Gagal menambah dosen. Periksa kembali form.')

    return render(req, 'dosens/index.html',{
        'data': tasks,
        'form' : form_input,
        'form_user' : form_user,
        'active_page': 'dosen'
    })

@login_required(login_url='/accounts/')
def update_staf(req, id):
    dosen = models.Dosen.objects.filter(pk=id).first()
    if req.POST:
        dosen.nama_dosen = req.POST.get('nama_dosen')
        dosen.nip = req.POST.get('nip')
        dosen.fakultas = req.POST.get('fakultas')
        dosen.jurusan = req.POST.get('jurusan')
        dosen.save()
        
        # Update email user jika ada perubahan
        if dosen.owner:
            email = req.POST.get('email')
            if email:
                dosen.owner.email = email
                dosen.owner.save()
                
        messages.success(req, f'Data Dosen {dosen.nama_dosen} telah diperbarui.')
        return redirect('/dosens/')

    return render(req, 'dosens/update.html', {
        'data': dosen,
        'active_page': 'dosen'
    })

@login_required(login_url='/accounts/')
def reset_password_dosen(req, id):
    dosen = models.Dosen.objects.filter(pk=id).first()
    if dosen and dosen.owner:
        # Generate random password atau set ke default (misal NIP)
        new_pass = dosen.nip 
        dosen.owner.set_password(new_pass)
        dosen.owner.save()
        messages.warning(req, f'Password {dosen.nama_dosen} telah di-reset menjadi NIP beliau.')
    return redirect('/dosens/')

@login_required(login_url='/accounts/')
def delete_staf(req, id):
    dosen = models.Dosen.objects.filter(pk=id).first()
    if dosen:
        nama = dosen.nama_dosen
        if dosen.owner:
            dosen.owner.delete()
        dosen.delete()
        messages.warning(req, f'Dosen {nama} dan akun terkait telah dihapus.')
    return redirect('/dosens/')
