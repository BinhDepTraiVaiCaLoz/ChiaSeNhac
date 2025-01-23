from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.form import CreateUserForm
from .models import *
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MusicSerializer

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công!")
            return redirect('home')
        else:
            if form.errors.get('username'):
                messages.info(request, "Username đã tồn tại. Vui lòng chọn username khác.")
    else:
        form = CreateUserForm()

    playlists = Playlist.objects.filter(is_sub=False)
    categories = Category.objects.filter(is_sub=False)

    context = {'form': form, 'playlists': playlists, 'categories': categories}
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

    playlists = Playlist.objects.filter(is_sub=False)
    categories = Category.objects.filter(is_sub=False)

    context = {'playlists': playlists, 'categories': categories}
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

def accountInfo(request):
    user = request.user
    playlists = Playlist.objects.filter(is_sub=False)
    categories = Category.objects.filter(is_sub=False)
    profile = Profile.objects.get(user=user)

    imgProfileUrl = profile.imgProfileUrl

    context = {'playlists': playlists, 'categories': categories, 'imgProfileUrl': imgProfileUrl}
    return render(request, 'app/account-info.html',context)


@login_required
def upload_avatar(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account-info')  # Điều hướng về trang thông tin tài khoản
    else:
        form = AvatarUploadForm(instance=profile)

    return render(request, 'account-info.html', {'form': form})