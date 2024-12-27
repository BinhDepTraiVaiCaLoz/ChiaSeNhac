from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']



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
    