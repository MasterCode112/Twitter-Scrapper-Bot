from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Login, register, create_account, login_view, index, User_Profile


urlpatterns = [
    path('', Login, name='login'),
    path('register/', register, name='register'),
    path('Creation/', create_account, name="create_account"),
    path('Login/', login_view, name="login_view"),
    path('Home/', index, name="index"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('Profile/', User_Profile, name="profile"),
]
