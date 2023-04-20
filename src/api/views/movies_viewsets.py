from rest_framework.viewsets import ModelViewSet
from api.models import Movie
from api.serializers import MovieSerializer
from api.permissions import AdminOrReadOnly

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AdminOrReadOnly]
