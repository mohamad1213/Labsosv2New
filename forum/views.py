from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mahasiswa.models import Pkl
# from catatan.models import Gambar
from . import models, forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/')
def index_mhs(req):
    forum = req.user.mahasiswa.first().nama_mitra

    return redirect(f'/forum/{forum.id}')

@login_required(login_url='/accounts/')
def index_dosen(req):
    tasks = req.user.membimbing.all()
    form_input = forms.ForumForm()

    if req.POST:
        form_input = forms.ForumForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/forumd/')

    return render(req, 'forumd/index.html',{
        'data': tasks,
        'form' : form_input,
    })

@login_required(login_url='/accounts/')
def index_staf(req):
    tasks = models.Forum.objects.all()
    form_input = forms.ForumForm()

    if req.POST:
        form_input = forms.ForumForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/forums/')

    return render(req, 'forums/index.html',{
        'data': tasks,
        'form' : form_input,
    })


@login_required(login_url='/accounts/')
def delete_forum(req, id):
    models.Forum.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/forums/')


@login_required(login_url='/accounts/')
def detail_forum(req, id):
    forum = models.Forum.objects.filter(pk=id).first() 
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()
    # form_gambar = forms.GambarForm()



    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))

        return redirect(f'/forums/{id}')

    return render(req, 'forums/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        # 'form_gambar' : form_gambar,
        'data': forum,
    })

@login_required(login_url='/accounts/')
def detail_forum_d(req, id):
    forum = models.Forum.objects.filter(pk=id).first()
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        return redirect(f'/forumd/{id}')
        

    return render(req, 'forumd/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        'data': forum,
    })

@login_required(login_url='/accounts/')
def detail_forum_mhs(req, id):
    forum = models.Forum.objects.filter(pk=id).first()
    komen = models.Komen.objects.filter(pk=id).first()
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        return redirect(f'/forum/{id}')


    return render(req, 'forum/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        'data': forum,
    })


@login_required(login_url='/accounts/')
def delete_posting(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forums/{id}')

@login_required(login_url='/accounts/')
def delete_posting_d(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forumd/{id}')

@login_required(login_url='/accounts/')
def delete_posting_mhs(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forum/{id}')
    
@login_required(login_url='/accounts/')
def delete_komen_mhs(req, id, id_posting, id_komen):
    models.Komen.objects.filter(pk=id_komen).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forum/{id}')

@login_required(login_url='/accounts/')
def delete_komen(req, id, id_komen):
    models.Komen.objects.filter(pk=id_komen).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forums/{id}/komen')

@login_required(login_url='/accounts/')
def delete_komen_d(req, id, id_komen):
    models.Komen.objects.filter(pk=id_komen).delete()
    messages.success(req, 'data telah di hapusid_posting')
    return redirect(f'/forumd/{id}/komen')


@login_required(login_url='/accounts/')
def staf_komen(req, id, id_posting):
    posting = models.Posting.objects.filter(pk=id_posting).first() 

    if req.POST:
        form_komen = forms.KomenForm(req.POST, req.FILES)
        if form_komen.is_valid():
            form_komen.instance.pengguna = req.user
            form_komen.instance.posting = posting
            form_komen.save()

    return redirect(f'/forums/{id}')

@login_required(login_url='/accounts/')
def dosen_komen(req, id, id_posting):
    posting = models.Posting.objects.filter(pk=id_posting).first() 

    if req.POST:
        form_komen = forms.KomenForm(req.POST, req.FILES)
        if form_komen.is_valid():
            form_komen.instance.pengguna = req.user
            form_komen.instance.posting = posting
            form_komen.save()

    return redirect(f'/forumd/{id}')
    
@login_required(login_url='/accounts/')
def mhs_komen(req, id, id_posting):
    posting = models.Posting.objects.filter(pk=id_posting).first() 

    if req.POST:
        form_komen = forms.KomenForm(req.POST, req.FILES)
        if form_komen.is_valid():
            form_komen.instance.pengguna = req.user
            form_komen.instance.posting = posting
            form_komen.save()

    return redirect(f'/forum/{id}')
def update_staf(req, id):
    if req.POST:
        forum = models.Forum.objects.filter(pk=id).update(
            nama_mitra=req.POST['nama_mitra'], 
            pic=req.POST['pic'], 
            alamat=req.POST['alamat'], 
            telp=req.POST['telp'],
            deskripsi=req.POST['deskripsi'])
        return redirect('/forums')

    forum = models.Forum.objects.filter(pk=id).first()    
    return render(req, 'forums/update.html', {
        'data': forum,
    })
