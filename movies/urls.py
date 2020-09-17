from django.contrib import admin
from django.urls import path

from movies.views import (
    moovie_list_view,
    create_movie,
    delete_movie,
    update_movie
)

urlpatterns = [
    path('movies', moovie_list_view),
    path('movies/create', create_movie),
    path('movies/delete', delete_movie),
    path('movies/update', update_movie),
]