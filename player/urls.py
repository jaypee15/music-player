from django.urls import path
from . import views

urlpatterns = [
    path("music/", views.IndexView.as_view(), name="index" ),
    path("music/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("music/album/add", views.AlbumCreateView.as_view(), name="album-add")
]