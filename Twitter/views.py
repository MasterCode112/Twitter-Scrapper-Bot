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
    # logger.info("Starting scraping operation....")
    # try:
    #     # Run the script and capture the output
    #     process = Popen(['python3', 'Twitter/Nitter/Scrapper_Boot_Twitter/scrapper_boot.py', '--since', '2023-05-03'], stdout=PIPE, stderr=PIPE)
    #     stdout, stderr = process.communicate()
    #     # Decode the output from bytes to string
    #     output = stdout.decode('utf-8')
    #     context = {'scraping_operation':output}
    #     logger.info("Scrapping operation completed successfully.")
    # except subprocess.CalledProcessError as e:
    #     logger.error(f"Scrapping operation failed: {e}")
    #     context = {'error_message': f"Scraping operation failed: {e}"}
    since = '2023-04-03'
    scrapper_boot.scrape(since=since, words='Tanzani', headless=False)
    data = scrapper_boot.scrape(since=since, words='Tanzani', headless=False)
    context = {'error_message' : data}
    return render(request, 'Admin/Scrapping_Operation.html', context)

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