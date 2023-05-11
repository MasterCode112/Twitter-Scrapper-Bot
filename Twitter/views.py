from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import os
import csv
from subprocess import Popen, PIPE
import logging
from .models import UserProfile
from Twitter.Nitter.Scrapper_Boot_Twitter import scrapper_boot


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

@login_required
def Twitter_scrapper(request):
    # file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'messagaes.txt')
    with open("Twitter/Nitter/Scrapper_Boot_Twitter/messagaes.txt") as f:
        message = f.read()
    context = {'messages' : message}
    return render(request, "Admin/Twitter-Scrapper.html", context)

@login_required
def Result_Scrapping_CSV(request):
    with open('Twitter/Nitter/Scrapper_Boot_Twitter/outputs/my_name_tanzania_uganda_2022-02-02_2023-04-03.csv', 'r') as f:
        reader = csv.DictReader(f)
        csv_data = [row for row in reader]
    context = {'csv_data': csv_data}
    return render(request, "Admin/Result_CSV.html", context)

@login_required
def Scrapping_Operation(request):
    since = '2023-04-03'
    data = "Twitter/Nitter/Scrapper_Boot_Twitter/messagaes.txt"

    if data is not None:
        with open(data, 'r') as f:
            words = f.read().strip().split('//')
    else:
        words = data.strip().split('//')

    scrapper_boot.scrape(since=since, words=words, headless=False)
    data = scrapper_boot.scrape(since=since, words=words,  headless=False)
    context = {'error_message' : data}
    return render(request, 'Admin/Scrapping_Operation.html')

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
            return redirect("login")

    return render(request, 'login.html')

def UserProfileUpdate(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        profile.country = request.POST['country']
        profile.address = request.POST['address']
        profile.phone = request.POST['phone']
        profile.save()
        
        if user and profile:
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Error updating profile')
        return redirect('../Profile')
    else:
        context = {'profile' : profile}
        return render(request, 'users_profile.html', context)


def ChangePassword(request):
    user = request.user
    if request.method == "POST":
        current_password = request.POST['currentPassword']
        password = request.POST['newPassword']
        if user.check_password(current_password):
            user.set_password(password)
            user.save()
            messages.success(request, 'Password updated successfully login again!')
        else:
            messages.error(request, 'Current password is incorrect.')
    return redirect('../')


