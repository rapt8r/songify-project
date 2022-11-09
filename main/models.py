from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.crypto import get_random_string
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG',optimize=True, quality="web_medium")
    new_image = File(im_io, name=image.name)
    return new_image

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=8, blank=True)
    slug = models.SlugField(max_length=32)
    profile_picture = models.ImageField(upload_to='author_profile_picture_images/')
    profile_background = models.ImageField(upload_to='author_profile_background_images/')

    def save(self, *args, **kwargs):
        original_size_profile_picture = self.profile_picture.size
        original_size_profile_background = self.profile_background.size

        compressed_profile_picture = compress(self.profile_picture)
        compressed_profile_background = compress(self.profile_background)

        compressed_size_profile_picture = compressed_profile_picture.size
        compressed_size_profile_background = compressed_profile_background.size

        self.profile_picture = compressed_profile_picture
        self.profile_background = compressed_profile_background
        print(f'Compression ended [{self.profile_picture.name}][{original_size_profile_picture}][{compressed_size_profile_picture}][{compressed_size_profile_picture-original_size_profile_picture}]')
        print(f'Compression ended [{self.profile_background.name}][{original_size_profile_background}][{compressed_size_profile_background}][{compressed_size_profile_background-original_size_profile_background}]')
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


def file_path(instance, filename):
     return f'{instance.title}/{filename}'

class Song(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=8, blank=True)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    number_of_plays = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to=file_path)
    music_file = models.FileField(upload_to=file_path)
    lyrics = models.TextField()

    def save(self, *args, **kwargs):
        original_size = self.cover_image.size
        compressed_cover_image = compress(self.cover_image)
        compressed_size = compressed_cover_image.size
        self.cover_image = compressed_cover_image
        if not self.slug:
            self.slug = get_random_string(length=8)
        print(f'Compression ended [{self.cover_image.name}][{original_size}][{compressed_size}][{compressed_size-original_size}]')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author.name} - {self.title}"

    class Meta:
        get_latest_by = "id"

class Playlist(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField(max_length=32)
    playlist_image = models.ImageField(upload_to='playlist_cover_images/')
    playlist_background = models.ImageField(upload_to='playlist_background_images/')
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
