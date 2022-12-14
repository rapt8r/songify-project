"""songify_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import AllSongsPage
from main.views import SearchPage
from main.views import main_page
from main.views import RegisterPage
from main.views import LogoutPage
from main.views import LoginPage
from main.views import AuthorPage
from main.views import AllAuthorsPage
from main.views import SongPage

from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', SearchPage.as_view(), name='SearchPage'),
    path('all-songs/', AllSongsPage.as_view(), name='AllSongs'),
    path('', main_page, name='MainPage'),


    path("register/", RegisterPage.as_view(), name='RegisterPage'),
    path("login/", LoginPage.as_view(), name='LoginPage'),
    path('authors/<slug:slug>', AuthorPage.as_view(), name='author_page'),
    path('authors/', AllAuthorsPage.as_view(), name='all_authors'),
    path("logout/", LogoutPage.as_view(), name='LogoutPage'),
    path("play/<slug:slug>", SongPage.as_view(), name='song_page'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

