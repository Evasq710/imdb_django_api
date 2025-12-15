from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

# GET ALL MOVIES
@api_view() # GET by default
def movie_list(request):
  # Complex datatype
  movies_qs = Movie.objects.all() # returns a QuerySet Object in the form of a list of registers

  # Serialization
  serializer = MovieSerializer(movies_qs, many=True) # many=True when using .all()

  # Render into JSON
  # serializer.data: <class 'rest_framework.utils.serializer_helpers.ReturnList'>
  return Response(serializer.data)


# GET A MOVIE
@api_view()
def movie_details(request, pk: int):
  # Complex datatype
  movie = Movie.objects.get(pk=pk)

  # Serialization
  serializer = MovieSerializer(movie)

  # Render into JSON
  # serializer.data: <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
  return Response(serializer.data)
