from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "all_albums"

    def get_queryset(self) -> QuerySet[Any]:
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = "detail.html"


class AlbumCreateView(generic.CreateView):
    model = Album
    fields = ["artist", "album_title", "genre", "album_logo"]
