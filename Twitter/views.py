from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

def Login(request):
    return render(request, 'login.html')

# Create your views here.
def register(request):
    return render(request, 'register.html')

@login_required
def index(request):
    return render(request, './Admin/index.html')

@login_required
def User_Profile(request):
    return render(request, 'Admin/users_profile.html')

@require_http_methods(['POST'])
def create_account(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if not (First_name and Last_name and email and username and password):
            messages.error(require, 'Please fill all required fields.')
            return redirect('../register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('../register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('../register')

        user = User.objects.create_user(first_name=First_name, last_name=Last_name, email=email, username=username, password=password)
        user.save()

        messages.success(request, 'Account created successfully.')
        return redirect('../register')

    return render(request, 'login.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'Logged in successfull.') 
            return redirect('../Home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect("../")

    return render(request, 'login.html')