from django.shortcuts import render
from main.models import Song
from random import choice, choices
from main.models import Author

# Create your views here.

MOTD_TEXT = [
    'Songify - to co lubisz, tak jak chcesz',
    'Songify - zabierz ze sobą',
    'Songify - twoja lista',
    'Songify - tak jak lubisz',
    'Songify - muzyka dla ciebie',
    'Songify - twoja muzyka',
    'Songify - twoje utwory',
    'Songify - słuchaj muzyki',
]
def MainPage(request):

    context_dir = {
        'trending_song': Song.objects.all().order_by('-number_of_plays')[0],
        'top_songs': Song.objects.all().order_by('-number_of_plays')[0:5],
        'recommended_artists': choices(Author.objects.all(), k=2),
        'motd': choice(MOTD_TEXT)
    }
    return render(request, template_name='main/main_page.html', context=context_dir)