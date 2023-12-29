from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="artist_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Album(models.Model):
    artist_id = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="albums"
    )
    name = models.CharField(max_length=500)
    cover = models.ImageField(upload_to="album_cover/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def __str__(self):
        return self.name + " - " + self.artist_id


class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    artist_id = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="songs"
    )
    title = models.CharField(max_length=50)
    length = models.FloatField(max_length=250)
    lyrics = models.TextField(blank=True)
    audio_file = models.FileField(upload_to="audio/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="playlists"
    )
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="playlist_covers/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PlaylistSong(models.Model):
    playlist_id = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="play_list_songs"
    )
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)


class Interaction(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_interactions"
    )
    song_id = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name="song_interactions"
    )
    liked = models.BooleanField(default=False)
    play_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
