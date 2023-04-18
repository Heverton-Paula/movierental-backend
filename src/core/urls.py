from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import movies_viewsets

router = routers.DefaultRouter()
router.register(r'movies', movies_viewsets.MovieViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
