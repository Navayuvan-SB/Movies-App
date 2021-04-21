from django.shortcuts import render
from django.views import generic
from .models import Movie, Genre, Studio, Director


class MovieListView(generic.ListView):
    model = Movie


class MovieDetailView(generic.DetailView):
    model = Movie


class GenreListView(generic.ListView):
    model = Genre


class GenreDetailView(generic.DetailView):
    model = Genre


class StudioListView(generic.ListView):
    model = Studio


class StudioDetailView(generic.DetailView):
    model = Studio


class DirectorListView(generic.ListView):
    model = Director