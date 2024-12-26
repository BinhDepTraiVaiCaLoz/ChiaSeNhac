from django import forms
from .models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm Password'
    )

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'slug', 'sub_playlist', 'is_sub']
    
    # Giới hạn các Playlist cha khi tạo playlist con
    sub_playlist = forms.ModelChoiceField(
        queryset=Playlist.objects.filter(is_sub=False),  # Chỉ cho phép chọn các playlist chính
        required=False,  # Nếu là playlist chính thì không cần chọn sub_playlist
        empty_label="Chọn playlist cha (nếu có)"
    )