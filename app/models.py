from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def imgProfileUrl(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return url
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if hasattr(instance, 'profile'):  # Kiểm tra nếu User đã có Profile
            instance.profile.save()

class Playlist(models.Model):
    sub_playlist = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_categories", null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_categories", null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.BooleanField(default=True)
    nation = models.CharField(max_length=150, null=True)
    singer_profile = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    category = models.ManyToManyField(Category, related_name="music_cate")
    playlist = models.ManyToManyField(Playlist, related_name="music_playlist")
    artist = models.ManyToManyField(Artist, related_name="music_artist")
    name = models.CharField(max_length=250, null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    duration_time = models.CharField(max_length=10, null=True)
    music_img = models.ImageField(upload_to='images/', null=True,blank=True)
    about = models.CharField(max_length=500, null=True)
    music_link = models.FileField(upload_to='audio/', default="Tôi hát")  # Tệp nhạc được tải lên

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.music_img.url
        except:
            url = ''
        return url
    
    @property
    def musicLink(self):
        try:
            url = self.music_link.url
        except:
            url = ''
        return url
    

