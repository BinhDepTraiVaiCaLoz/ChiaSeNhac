from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('api/musics/', views.MusicListAPI.as_view(), name='music-list-api'),
    path('account-info/', views.accountInfo, name="account-info"),
]
