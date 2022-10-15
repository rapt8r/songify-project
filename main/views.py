from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, RedirectView
from main.models import Song, Author, Playlist
from random import choice, choices, sample
from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LogoutView, LoginView
from main.forms import AuthForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SearchPage(TemplateView):
    template_name = 'main/search_page.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Pobieranie parametru q z adresu url (np: songify.com/search?q=)
        query = request.GET.get('q', 'all')
        context['songs_search_result'] = Song.objects.filter(title__contains=query).all()
        context['authors_search_result'] = Author.objects.filter(name__contains=query).all()
        context['playlists_search_result'] = Playlist.objects.filter(name__contains=query).all()
        return self.render_to_response(context)


class RegisterPage(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('LoginPage')
    form_class = UserRegisterForm
    success_message = "Zarejestrowano pomyślnie!"


class LoginPage(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthForm


class LogoutPage(SuccessMessageMixin, LogoutView):
    success_message = 'Zostałeś wylogowany'
    next_page = 'LoginPage'


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
NEW_SONG_LABEL = [
    'Check out my new song - ',
    'New release - ',
    'Latest release - '
]

def main_page(request):
    context_dir = {
        'new_song_label': choice(NEW_SONG_LABEL),
        'new_song': Song.objects.latest(),
        'choosen_for_you': sample(list(Song.objects.all()), 5),
        'discover_new_artists': sample(list(Author.objects.all()), 5),
        'motd': choice(MOTD_TEXT),
    }
    return render(request, template_name='main/main_page.html', context=context_dir)


class AuthorPage(DetailView):
    model = Author
    template_name = 'main/author_page.html'
    slug_field = 'slug'
    context_object_name = 'author'


class AllAuthorsPage(ListView):
    model = Author
    template_name = 'main/all_authors_page.html'
    context_object_name = 'list'


class AllSongsPage(ListView):
    model = Song
    template_name = 'main/all_songs_page.html'
    context_object_name = 'list'

class SongPage(LoginRequiredMixin,DetailView):
    model = Song
    template_name = 'main/song_page.html'
    slug_field = 'slug'
    context_object_name = 'song'

    def get_object(self):
        obj = super().get_object()
        obj.number_of_plays += 1
        obj.save(update_fields=['number_of_plays'])
        return obj
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['up_next'] = sample(list(Song.objects.all()), 5)
        return self.render_to_response(context)