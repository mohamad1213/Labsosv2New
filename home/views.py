from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from mahasiswa.models import Pkl
from catatan import models, forms
from forum.models import Forum
from dosen.models import Dosen
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()



@login_required(login_url='/accounts/')
def index(req):
    group = req.user.groups.first()
    
    if group is not None and group.name == 'dosen':
        # Dashboard Dosen: Data Riil
        students_all = Pkl.objects.filter(nama_dosen=req.user)
        total_mhs = students_all.count()
        mhs_aktif = students_all.filter(approve=True, approve2=True).count()
        mhs_pending = students_all.filter(approve=True, approve2=False, reject2=False).count()
        
        # Ambil logbook terbaru dari mahasiswa bimbingan
        mahasiswa_ids = students_all.values_list('owner_id', flat=True)
        latest_logs = models.Catatan.objects.filter(owner_id__in=mahasiswa_ids).order_by('-waktu')
        log_count = latest_logs.count()
        
        return render(req, 'dosen/index.html', {
            'active_page': 'dashboard',
            'total_mhs': total_mhs, # for backward compatibility if any
            'mhs_aktif_count': mhs_aktif,
            'pkl_pending_count': mhs_pending,
            'pkl_appr_count': mhs_aktif, # Active as approved
            'log_count': log_count,
            'latest_logs': latest_logs[:5],
            'students': students_all[:5],
        })
        
    elif group is not None and group.name == 'staf':
        # Dashboard Staf: Data Riil
        students_all = Pkl.objects.all()
        k_total = students_all.count()
        k_pend = students_all.filter(approve=False, reject=False).count()
        k_appr = students_all.filter(approve=True, approve2=True).count()
        k_rej = students_all.filter(reject=True).count()
        
        # Ambil data Mitra dan Dosen
        mitra_list = Forum.objects.all()
        k_mitra = mitra_list.count()
        dosen_list = Dosen.objects.all()

        # Ambil logbook terbaru dari semua mahasiswa (untuk Staf)
        mahasiswa_ids = students_all.values_list('owner_id', flat=True)
        latest_logs = models.Catatan.objects.filter(owner_id__in=mahasiswa_ids).order_by('-waktu')
        log_count = latest_logs.count()
        
        # Ambil aktivitas terbaru (PKL baru atau status berubah)
        latest_activities = models.Catatan.objects.all().order_by('-waktu')[:5]
        print(latest_activities)
        return render(req, 'staf/index.html', {
            'active_page': 'dashboard',
            'k_total': k_total,
            'k_pend': k_pend,
            'k_appr': k_appr,
            'k_rej': k_rej,
            'k_mitra': k_mitra,
            'log_count': log_count,
            'latest_logs': latest_logs[:5],
            'latest_activities': latest_activities,
            'mitra_list': mitra_list[:5],
            'dosen_list': dosen_list[:5],
        })
    else:
        # Dashboard Mahasiswa
        from mahasiswa.views import index as mahasiswa_index
        return mahasiswa_index(req)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


@login_required(login_url='/accounts/')
def delete_catatan(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/')

@login_required(login_url='/accounts/')
def cetak(req):
    # Ambil data PKL user ini
    pkl_obj = Pkl.objects.filter(owner=req.user).first()
    
    # Ambil semua logbook user ini
    logbooks = models.Catatan.objects.filter(owner=req.user).order_by('waktu')
    
    # Ambil profil dosen pembimbing jika ada
    dosen_obj = None
    if pkl_obj and pkl_obj.nama_dosen:
        dosen_obj = Dosen.objects.filter(owner=pkl_obj.nama_dosen).first()

    return render(req, 'home/cetak.html', {
        'cetak' : logbooks,
        'pkl' : pkl_obj,
        'dosen' : dosen_obj,  
        'user' : req.user
    })


@login_required(login_url='/accounts/')
def cetak_dosen(req):
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'dosen/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
    })


@login_required(login_url='/accounts/')
def cetak_staf(req):
    group = req.user.groups.first() 
    cetak = [] 
    if group is not None and group.name == 'staf':
        cetak = models.Catatan.objects.filter(owner=req.user)
    
    return render(req, 'staf/cetak.html', {
        'cetak' : cetak,
    })