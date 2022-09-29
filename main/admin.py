from django.contrib import admin
from .models import Song, Author, Category, Playlist

admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Playlist)