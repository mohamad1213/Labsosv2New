from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm, UserProfileForm
from mahasiswa.models import Pkl
from django.conf import settings 
from django.core.mail import send_mail 

# from verify_email.email_handler import send_verification_email
from .models import *

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				group = Group.objects.get(name='mahasiswa') 
				user.groups.add(group)
				subject = 'Selamat Datang di SIM-Labsos'
				message = f'Hi {user.username}, thank you for registering in SIM-Labsos'
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [user.email, ] 
				send_mail( subject, message, email_from, recipient_list ) 

				# inactive_user.cleaned_data['email']
				# inactive_user = send_verification_email(request, form)
				return redirect('/accounts/')
			else:
				print(form.errors)
		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/accounts/')

def accountSettings(req):
	tasks = Pkl.objects.filter(owner=req.user)
	forum = Forum.objects.filter().first()
	biodata = UserProfile.objects.filter(owner=req.user).first()
	pkl = Pkl.objects.filter(owner=req.user).first()
	# dosen = Dosen.objects.filter(owner=req.user).first()
	return render(req, 'accounts/profile.html',{
		'data': tasks,
		'forum' :forum, 
		'pkl' :pkl,
		# 'dosen':dosen,
		'biodata':biodata,
		})

def accountSettings_staf(req):
	tasks = Pkl.objects.filter(owner=req.user)
	forum = Forum.objects.filter().first()
	biodata = UserProfile.objects.filter(owner=req.user).first()
	pkl = Pkl.objects.filter(owner=req.user).first()
	# dosen = Dosen.objects.filter(owner=req.user).first()
	return render(req, 'accounts/profilestaf.html',{
		'data': tasks,
		'forum' :forum, 
		'pkl' :pkl,
		# 'dosen':dosen,
		'biodata':biodata,
		})
def accountSettings_dosen(req):
	tasks = Pkl.objects.filter(owner=req.user)
	forum = Forum.objects.filter().first()
	biodata = UserProfile.objects.filter(owner=req.user).first()
	pkl = Pkl.objects.filter(owner=req.user).first()
	# dosen = Dosen.objects.filter(owner=req.user).first()
	return render(req, 'accounts/profiledosen.html',{
		'data': tasks,
		'forum' :forum, 
		'pkl' :pkl,
		# 'dosen':dosen,
		'biodata':biodata,
		})
# def accountSettings(request):
# 	customer = request.user.customer
# 	form = CustomerForm(instance=customer)

# 	if request.method == 'POST':
# 		form = CustomerForm(request.POST, request.FILES,instance=customer)
# 		if form.is_valid():
# 			form.save()


# 	context = {'form':form}
# 	return render(request, 'accounts/account_settings.html', context)



def edit(req):
	tasks = models.UserProfile.objects.filter(owner=req.user)
	profile = req.user.profile
	form = UserProfileForm(instance=profile)
	if req.method == 'POST':
		form = UserProfileForm(req.POST, req.FILES, instance=profile)
		if form.is_valid():
			# form.instance.owner=req.user
			form.save()

			# return redirect('/accounts')
	# else:
	# 	messages.error(req, 'A problem has been occurred while submitting your data.')
		context = {'form':form,'data':tasks}
		return render(req, 'accounts/profile.html',context)

@login_required(login_url='/accounts/')
def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })
