from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Audio
from django.contrib.auth.decorators import login_required
from .forms import UploadForm,CreateUserForm,LoginForm
from django.contrib.auth.models import User
from .decorators import unauthenticated_user, allowed_users, admin_only

# 0776038999 ~ joel


# Create your views here.
@login_required
@allowed_users(['admin'])
def admin_dashboard(request):
    """
    Displays all the audios uploaded by all the various users
    """
    audio = Audio.objects.all()
    return render(request, 'home.html', {'audio':audio})

@login_required
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'form.html', {'form': UploadForm})

@login_required
def how_to_upload(request):
    return render (request, 'how_to_upload.html')


@unauthenticated_user
def register_user(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CreateUserForm()
	return render (request,"register.html", context={"form":form})

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
                messages.success(request,("Password or Username Incorrect!!"))
    return render(
    request,'registration/login.html',context={'form':form, 'message':message}
    )


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    audio = request.user.audio_set.all()
    return render(request, 'user.html', {'audio':audio})
