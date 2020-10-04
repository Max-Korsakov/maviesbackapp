from django.contrib import admin
from django.urls import path

from movies.views import (
    moovie_list_view,
    create_movie,
    delete_movie,
    update_movie,
    get_movie_by_id
)

urlpatterns = [
    path('movies', moovie_list_view),
    path('movies/<str:id>/', get_movie_by_id),
    path('movies/create', create_movie),
    path('movies/delete', delete_movie),
    path('movies/update', update_movie),
]
