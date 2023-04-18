from django.contrib import admin
from .models.movies import Movie
# Register your models here.

class Movies(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'genre', 'release_date', 'director')
    list_display_links = ('id', 'title', 'description', 'genre', 'director')

admin.site.register(Movie, Movies)