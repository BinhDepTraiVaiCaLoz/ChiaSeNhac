from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Profile)