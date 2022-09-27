from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=32)
    profile_picture = models.ImageField(upload_to='author_profile_picture_images/')
    profile_background = models.ImageField(upload_to='author_profile_background_images/')

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=8)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    number_of_plays = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to='song_cover_images/')
    music_file = models.FileField(upload_to='song_files')
    lyrics = models.TextField()

    def __str__(self):
        return f"{self.author.name} - {self.title}"


class Playlist(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField(max_length=32)
    playlist_image = models.ImageField(upload_to='playlist_cover_images/')
    playlist_background = models.ImageField(upload_to='playlist_background_images/')
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
