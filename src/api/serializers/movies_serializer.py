from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from ..models.movies import Movie
from api.permissions import ReadOnly

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
