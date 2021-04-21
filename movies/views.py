from django.shortcuts import render
from django.views import generic
from .models import Movie


class MovieListView(generic.ListView):
    model = Movie


class MovieDetailView(generic.DetailView):
    model = Movie
