from rest_framework import serializers
from .models import Music, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)  # Serialize nghệ sĩ nhiều giá trị

    class Meta:
        model = Music
        fields = ['id', 'name', 'artist', 'music_link', 'music_img', 'about']