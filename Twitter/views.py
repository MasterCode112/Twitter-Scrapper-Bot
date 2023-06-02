from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import time
import csv
from subprocess import Popen, PIPE
import logging
import os
from .models import UserProfile, C_Settings, D_Settings
from Twitter.Nitter.Scrapper_Boot_Twitter import scrapper_boot, scrapper_boot_single
from django.views.decorators.cache import never_cache

def Login(request):
    return render(request, 'login.html')

# Create your views here.
def register(request):
    return render(request, 'register.html')

@never_cache
def index(request):
    return render(request, './Admin/index.html')

@never_cache
def User_Profile(request):
    return render(request, 'Admin/users_profile.html')


def Twitter_scrapper(request):
    # file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'messagaes.txt')
    with open("Twitter/Nitter/Scrapper_Boot_Twitter/messagaes.txt") as f:
        message = f.read()
    context = {'messages' : message}
    user = request.user
    try:
        custom_settings = C_Settings.objects.get(user=user)
        context['to_account'] = custom_settings.to_account
        context['mention_account'] = custom_settings.mention_account
        context['from_account'] = custom_settings.from_account
        context['headless'] = custom_settings.headless
        context['display_type'] = custom_settings.display_type
        context['interval'] = custom_settings.interval
        context['proxy'] = custom_settings.proxy
        context['resume'] = custom_settings.resume
    except C_Settings.DoesNotExist:
        danger = "There no data found in table.!"
        context = {'messages' : message, 'danger' : danger}
        return render(request, "Admin/Twitter-Scrapper.html", context)
    
    if request.method == "POST":
        mention_account = request.POST['TargetedAccount']
        from_account = request.POST['FromAccount']
        to_account = request.POST['ToAccount']
        headless = request.POST['Headless']
        display_type = request.POST['Display_type']
        interval = request.POST['Interval']
        proxy = request.POST['proxy']
        words = request.POST['Dictionary']
        resume = request.POST['resume']

        try:
            custom_settings = C_Settings.objects.get(user=user)
            custom_settings.mention_account = mention_account
            custom_settings.from_account = from_account
            custom_settings.to_account = to_account
            custom_settings.headless = headless
            custom_settings.display_type = display_type
            custom_settings.interval = interval
            custom_settings.proxy = proxy
            custom_settings.words = words
            custom_settings.resume = resume
            custom_settings.save()
            if custom_settings:
                success = "Custom settings updated successfully!"
                context = {'messages' : message, 'success' : success}
                return render(request, "Admin/Twitter-Scrapper.html", context)
        except C_Settings.DoesNotExist:
            custom_settings = C_Settings(user=user, mention_account=mention_account, from_account=from_account, to_account=to_account,
                                         headless=headless, display_type=display_type, interval=interval, proxy=proxy, resume=resume)
            custom_settings.save()
            if custom_settings:
                danger = "Custom settings saving successfully!"
                context = {'messages' : message, 'success' : danger}
                return render(request, "Admin/Twitter-Scrapper.html", context)


    return render(request, "Admin/Twitter-Scrapper.html", context)

def scrapping_setup(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == "POST":
            profile.status_scraping = request.POST['status_scraping']
            profile.save()
            if profile:
                success = "Settings changed successfully!"
                context = {'success' : success}
                return render(request, "Admin/Twitter-Scrapper.html", context)
            else:
                danger = "Something wrong!"
                context = {'danger' : danger}
                return render(request, "Admin/Twitter-Scrapper.html", context)
    return render(request, "Admin/Twitter-Scrapper.html")

@never_cache
def Result_Scrapping_CSV(request):
    directory = 'Twitter/Nitter/Scrapper_Boot_Twitter/outputs'
    files = os.listdir(directory)
    file_links = []
    latest_file = None
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_link = {
                'link': f'{directory}/{file}',
                'modified': os.path.getmtime(file_path),
            }
            if latest_file is None or file_link['modified'] > latest_file['modified']:
                latest_file = file_link
            file_links.append(file_link)
    csv_data = None
    if latest_file is not None:
        with open(latest_file['link'], 'r') as f:
            reader = csv.DictReader(f)
            csv_data = [row for row in reader]
    context = {
        'csv_data': csv_data,
        'file_links': file_links,
        'latest_file': latest_file,
    }
    return render(request, 'Admin/Result_CSV.html', context)

def open_file(request, file_name):
    file_path = os.path.join('Twitter/Nitter/Scrapper_Boot_Twitter/outputs', file_name)
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        csv_data = [row for row in reader]
    context = {'csv_data': csv_data}
    return render(request, "Admin/Result_CSV.html", context)


@never_cache
def Scrapping_Operation(request):
    return render(request, 'Admin/Scrapping_Operation.html')

def enable_scrapping(request):
    if request.method == 'POST':
        data = ""
        progress = 0
        context = {'progress': progress, 'data': data}
        
        # Render template
        # return render(request, 'Admin/Scrapping_Operation.html', context=context)

        since = '2023-05-03'
        word = "Twitter/Nitter/Scrapper_Boot_Twitter/messagaes.txt"

        if word is not None:
            with open(word, 'r') as f:
                words = f.read().strip().split('//')
        else:
            words = word.strip().split('//')

        # Start scraping
        progress = 0
        while progress < 100:
            time.sleep(1)
            progress += 1

        user = request.user
        profile_data = UserProfile.objects.get(user=user)
        if profile_data.status_scraping == "d_settings":
            scrapper_boot.scrape(since=since, words=words, headless=False)
            data = scrapper_boot.scrape(since=since, words=words, headless=False, save_dir="Twitter/Nitter/Scrapper_Boot_Twitter/outputs/")
        else:
            customer_data = C_Settings.objects.get(user=user)
            words = customer_data.words
            # since = customer_data.since.strftime('%Y-%m-%d')
            # headless = customer_data.headless
            # until = customer_data.until.strftime('%Y-%m-%d')
            to_account = customer_data.to_account
            from_account = customer_data.from_account
            # mention_account = customer_data.mention_account
            # resume = customer_data.resume
            # proxy = customer_data.proxy
            # proximity = customer_data.proximity
            # geocode = customer_data.geocode
            # lang = customer_data.lang
            # minreplies = customer_data.minreplies
            # minlikes = customer_data.minlikes
            # minretweets = customer_data.minretweets
            # display_type = customer_data.display_type
            # hashtag = customer_data.hashtag

            scrapper_boot_single.scrape(since=since, words=words, from_account=from_account, headless=False)
            data = scrapper_boot_single.scrape(since=since,  words=words, from_account=from_account, headless=False, save_dir="Twitter/Nitter/Scrapper_Boot_Twitter/outputs/")
        
        # Pass data as context variable
        context = {'progress': progress, 'data': data}
        
        # Render template
        return render(request, 'Admin/Scrapping_Operation.html', context=context)

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

@never_cache
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

@never_cache
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

@never_cache
def default_scraping(request):
    user = request.user
    try:
        custom_settings = D_Settings.objects.get()
        context['D_to_account'] = custom_settings.to_account
        context['D_mention_account'] = custom_settings.mention_account
        context['D_from_account'] = custom_settings.from_account
        context['D_headless'] = custom_settings.headless
        context['D_display_type'] = custom_settings.display_type
        context['D_interval'] = custom_settings.interval
        context['D_proxy'] = custom_settings.proxy
        context['resume'] = custom_settings.resume
    except D_Settings.DoesNotExist:
        # handle case where the user has no settings yet
        pass
        
@never_cache
def dictionary_management(request):
    file_path = "Twitter/Nitter/Scrapper_Boot_Twitter/messagaes.txt"

    with open(file_path) as f:
        message = f.read()
        
    context = {"messages": message }
    
    if request.method == "POST":
        dictionary = request.POST.get('Dictionary')
        if dictionary:
            try:
                with open(file_path, 'w') as f:
                    f.write(dictionary)
                context['success'] = "The word was changed successfully!"
                return redirect('dictionary_management')
            except Exception as e:
                context['error'] = "There was an error adding the word." + str(e)
                # print(e)
        else:
            context['error'] = "Please enter a word to add."
        
    return render(request, "Admin/ManageDictionaries.html", context)