from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
  template_name = 'movie_list.html'   # assign html template
  model = Movie                       # assign model access to view
  context_object_name = 'movies'


class MovieDetailsView(DetailView):
  template_name = 'movie_detail.html'
  model = Movie

