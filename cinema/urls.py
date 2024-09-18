from django.urls import path

from cinema.views import movies, movie_detail


app_name = "cinema"

urlpatterns = [
    path("movies/", movies, name="movies"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
