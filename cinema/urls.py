from django.urls import path

from .views import movies


app_name = "cinema"

urlpatterns = [
    path("movies/", movies, name="movies"),
]
