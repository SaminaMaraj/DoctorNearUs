from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'doctors/index.html', {})

def login_page(request):
    return render(request, 'doctors/login.html', {})

def login(request):
    print("##############################################")
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        auth.login(request.user)
        return redirect('index')
    else:
        return redirect('login_page')

def signup(request):
    return render(request, 'doctors/registration.html', {})

def create_account(request):
    print("##############################################")
    print(request.POST['username'], request.POST['email'], request.POST['password'], request.POST['fname'], request.POST['lname'], request.POST['dob'])
    user = User.objects.filter(username=request.POST['username'])

    if user.exists():
        return redirect('signup')
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'],
                                        first_name=request.POST['fname'],
                                        last_name=request.POST['lname'])
        return redirect('login_page')
