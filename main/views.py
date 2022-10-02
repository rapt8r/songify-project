from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Song, Author, Playlist
from random import choice, choices

# Create your views here.

class SearchPage(TemplateView):
    template_name = 'main/search_page.html'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        #Pobieranie parametru q z adresu url (np: songify.com/search?q=)
        query = request.GET.get('q', 'all')
        context['songs_search_result'] = Song.objects.filter(title__contains=query).all()
        context['authors_search_result'] = Author.objects.filter(name__contains=query).all()
        context['playlists_search_result'] = Playlist.objects.filter(name__contains=query).all()
        return self.render_to_response(context)

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
        'top_songs': Song.objects.all().order_by('-number_of_plays')[1:4],
        'recommended_artists': choices(Author.objects.all(), k=2),
        'motd': choice(MOTD_TEXT),
        'top_playlist': Playlist.objects.all()
    }
    return render(request, template_name='main/main_page.html', context=context_dir)