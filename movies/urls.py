from django.urls import path
from . import views

urlpatterns = [
    path("", views.MovieListView.as_view(), name="movies"),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("genres/", views.GenreListView.as_view(), name="genres"),
    path("genres/<slug:slug>/", views.GenreDetailView.as_view(), name="genre-detail"),
    path("studios/", views.StudioListView.as_view(), name="studios"),
    path(
        "studios/<slug:slug>/", views.StudioDetailView.as_view(), name="studio-detail"
    ),
    path("directors/", views.DirectorListView.as_view(), name="directors"),
    path(
        "directors/<slug:slug>/", views.DirectorDetailView.as_view(), name="director-detail"
    ),
]
