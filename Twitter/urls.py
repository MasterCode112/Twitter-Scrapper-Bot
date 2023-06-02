from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Login, register, create_account, default_scraping, scrapping_setup, dictionary_management, login_view, open_file, enable_scrapping, index, User_Profile, Twitter_scrapper, Result_Scrapping_CSV, Scrapping_Operation, UserProfileUpdate, ChangePassword


urlpatterns = [
    path('', Login, name='login'),
    path('register/', register, name='register'),
    path('Creation/', create_account, name="create_account"),
    path('Login/', login_view, name="login_view"),
    path('Home/', index, name="index"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('Profile/', User_Profile, name="profile"),
    path('TwitterScrapper/', Twitter_scrapper, name="TwitterScrapper"),
    path('Result_SCV/', Result_Scrapping_CSV, name="Result_CSV"),
    path('Operation/', Scrapping_Operation, name='Operation'),
    path('update_user/', UserProfileUpdate, name='update_user'),
    path('changepassword/', ChangePassword, name='changepassword'),
    path('enabled', enable_scrapping, name="enabled"),
    path('open_file/', open_file, name='open_file'),
    path('dictionary/', dictionary_management, name='dictionary_manage'),
    path('setupScraping', scrapping_setup, name="setup"),
    path('DefaultSettings', default_scraping, name="d_settings"),
]
