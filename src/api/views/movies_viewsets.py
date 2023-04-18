from rest_framework.viewsets import ModelViewSet
from ..models.movies import Movie
from ..serializers.movies_serializer import MovieSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer