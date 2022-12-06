from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import UploadForm,CreateUserForm
from django.contrib.auth.models import User

# Create your views here.

from .decorators import unauthenticated_user, allowed_users, admin_only

# 0776038999 ~ joel


@unauthenticated_user
def register_user(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home2")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CreateUserForm()
	return render (request=request, template_name="auth/register.html", context={"form":form})

@unauthenticated_user
def login_user(request):
    form = forms.LoginForm()
    message = ''
    user = User()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            #family = form.cleaned_data['family']
            )
            if user is not None:
                login(request,user)
                #message = f'Hello {user.username}! Login Successful'
                messages.success(request,(f'Welcome back {user.username}!'))
                return redirect('home')
            else:
                #message = 'username or password incorrect'
                messages.success(request,("There Was an Logging In, Try Again...."))
    return render(
    request,'auth/login.html',context={'form':form, 'message':message}
    )

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home2(request):
    document = request.user.document_set.all()

    return render(request, 'auth/home.html', {'document':document})


@login_required
def upload(request):
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home2')

    return render(request, './form.html', {'form': UploadForm})
