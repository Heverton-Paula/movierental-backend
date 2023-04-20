from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import users_viewsets
from api.views import movies_viewsets

router = routers.DefaultRouter()
router.register('users', users_viewsets.UserViewSet)
router.register('movies', movies_viewsets.MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
