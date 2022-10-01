from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Song, Author, Playlist
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