from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.form import CreateUserForm
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MusicSerializer

# Create your views here.
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'User or password is invalid')

    context = {}
    return render(request, 'app/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')



def home(request):
    playlists = Playlist.objects.filter(is_sub=False)
    categories = Category.objects.filter(is_sub=False)
    musics = Music.objects.all()
    context = {'playlists':playlists, 'categories': categories, 'musics': musics}
    return render(request,'app/home.html',context)


class MusicListAPI(APIView):
    def get(self, request):
        musics = Music.objects.all()  # Lấy toàn bộ bài hát
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
