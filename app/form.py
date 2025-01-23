from django import forms
from .models import *


# Create your models here.
class CreateUserForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Lưu ảnh đại diện vào Profile model
            Profile.objects.get_or_create(
                user=user,
                profile_picture=self.cleaned_data.get('profile_picture')
            )
        return user


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


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }