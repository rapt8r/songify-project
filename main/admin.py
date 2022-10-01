from django.contrib import admin
from .models import Song, Author, Category, Playlist

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'profile_picture')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'number_of_plays')
    search_fields = ['name', 'category']
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ['name', 'slug']

admin.site.register(Song, SongAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Playlist, PlaylistAdmin)