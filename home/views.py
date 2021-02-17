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
    data_labsos = Pkl.objects.all()
    count_data_labsos = len(data_labsos)
    user = User.objects.filter(groups__name='mahasiswa')
    count_user = len(user)
    dosen = Dosen.objects.all()
    count_dosen = len(dosen)
    # form_input = forms.DosenForm()
    tasks = models.Catatan.objects.filter(owner=req.user)
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()

    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/')

    group = req.user.groups.first()
    if group is not None and group.name == 'dosen':
        return render(req, 'dosen/index.html')
    elif group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all()
        return render(req, 'staf/index.html')
    else:
        return render(req, 'home/index.html', {
            'data': tasks,
            # 'form' : form_input,
            'form_catatan' : form_catatan,
            'form_gambar' : form_gambar,
            'count_data_labsos': count_data_labsos,
            'count_user': count_user,  
            'count_dosen':count_dosen, 
        })
    return render(req, 'staf/index.html')

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
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'home/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
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
    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'staf': # mendefinisikan bahwa ini adalah dosen
        cetak = models.Catatan.objects.filter(owner=req.user)
    # return redirect(f'/home/{id}')
    return render(req, 'staf/cetak.html', {
        'cetak' : cetak,
    })