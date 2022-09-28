from main.models import Category, Author, Song, Playlist
from django.core.files import File
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from random import randint
DEFAULT_BACKGROUND = 'dev_tools/src/default_background.png'
DEFAULT_PLAYLIST_IMG = 'dev_tools/src/default_playlist_img.jpg'
MEDIA_FOLDER = 'dev_tools/src/'
#Dummy category data used to fill up database for testing
DUMMY_CATEGORY = [
    {'name' : 'POP'},
    {'name' : 'RAP'},
    {'name' : 'ROCK'},
    {'name' : 'TRAP'},
    {'name' : 'HIP-HOP'},
    {'name' : 'LATINO'},
    {'name' : 'KOŚCIELNA'},
]
#Dummy author data used to fill up database for testing
DUMMY_AUTHOR = [
    {'name': 'Krzysztof Krawczyk', 'description': 'Dzień dobry, jestem Krzysztof Krawczyk!', 'profile_picture': 'krawczyk.png'},
    {'name': 'Maryla Rodowicz', 'description': 'Rozmrażają mnie co sylwestra...', 'profile_picture': 'rodowicz.png'},
    {'name': 'Zenon Martyniuk', 'description': 'Gwiazda, w górze lśni', 'profile_picture': 'martyniuk.png'},
    {'name': 'Doda', 'description': 'Szukam miłości', 'profile_picture': 'doda.png'},
    {'name': 'Zespół Marzenie', 'description': 'W moim ogródeczku!', 'profile_picture': 'marzenie.png'},
    {'name': 'Imagine Dragons', 'description': 'We make good music', 'profile_picture': 'imagine_dragons.png'},
    {'name': 'Camila Cabello', 'description': 'Latino girl!', 'profile_picture': 'cabello.png'},
    {'name': 'The Undertaker', 'description': 'I will find you...', 'profile_picture': 'undertaker.png'},
]
#Dummy song data used to fill up database for testing
DUMMY_SONG = [
    {'title': 'Bones', 'author': 'Imagine Dragons', 'category': 'POP', 'cover_image': 'bones.png', 'music_file': 'bones.mp3', 'lyrics': 'Gimmi gimmi some time to think...'},
    {'title': 'Don\'t go yet', 'author': 'Camila Cabello', 'category': 'LATINO', 'cover_image': 'yet.png', 'music_file': 'yet.mp3', 'lyrics': 'Oyee, don\t go yet!'},
    {'title': 'Theme Song', 'author': 'The Undertaker', 'category': 'KOŚCIELNA', 'cover_image': 'theme.png', 'music_file': 'theme.mp3', 'lyrics': 'No text'},
]
#Dummy playlist data used to fill up database for test
DUMMY_PLAYLIST = [
    {'name': 'Najpopularniejsze, teraz!', 'description': 'Wszystkie popularne kawałki na jednej playliście'}
]

def fill_up():
    """
    Fills up the database with dummy data
    """
    print('====CATEGORY====')
    for category in DUMMY_CATEGORY:
        new_category = Category()
        new_category.name = category['name']
        new_category.save()
        print(f"Added {category['name']} to database.")
    print('====AUTHOR====')
    for author in DUMMY_AUTHOR:
        new_author = Author()
        new_author.name = author['name']
        new_author.description = author['description']
        new_author.slug = slugify(author['name'])
        new_author.profile_picture = File(open(MEDIA_FOLDER + author['profile_picture'], 'rb'))
        new_author.profile_background = File(open(DEFAULT_BACKGROUND, 'rb'))
        new_author.save()
        print(f"Added {author['name']} to database.")
    print('====SONG====')
    for song in DUMMY_SONG:
        new_song = Song()
        new_song.title = song['title']
        new_song.slug = get_random_string(length=8)
        new_song.number_of_plays = randint(1, 500)
        new_song.cover_image = File(open(MEDIA_FOLDER + song['cover_image'], 'rb'))
        new_song.music_file = File(open(MEDIA_FOLDER + song['music_file'], 'rb'))
        new_song.lyrics = song['lyrics']
        new_song.save()
        new_song.author.set(Author.objects.filter(name__exact=song['author']))
        new_song.category.set(Category.objects.filter(name__exact=song['category']))
        print(f"Added {song['title']} to database.")
    print('====PLAYLIST====')
    for playlist in DUMMY_PLAYLIST:
        new_playlist = Playlist()
        new_playlist.name = playlist['name']
        new_playlist.description = playlist['description']
        new_playlist.slug = slugify(playlist['name'])
        new_playlist.playlist_image = File(open(DEFAULT_PLAYLIST_IMG, 'rb'))
        new_playlist.playlist_background = File(open(DEFAULT_BACKGROUND, 'rb'))
        new_playlist.save()
        new_playlist.songs.set(Song.objects.all().order_by('-number_of_plays'))
        print(f"Added {playlist['name']} to database.")
    print('Done...')