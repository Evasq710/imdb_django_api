from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.

# GET ALL MOVIES
def movie_list(request):
  movies_qs = Movie.objects.all() # returns a QuerySet Object in the form of a list of registers
  movies = movies_qs.values() # returns a QuerySet Object in the form of a list of python dictionaries
  data = {
    'movies': list(movies) # list() will transform QuerySet Object into a list of valid python dictionaries
  }

  return JsonResponse(data)


# GET AN SPECIFIC MOVIE
def movie_details(request, pk):
  movie = Movie.objects.get(pk=pk) # returns a Movie Object if found
  data = {
    'name': movie.name,
    'description': movie.description,
    'active': movie.active,
  }

  return JsonResponse(data)