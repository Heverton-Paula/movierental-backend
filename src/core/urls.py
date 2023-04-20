from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import users_viewsets
from api.views import movies_viewsets
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = routers.DefaultRouter()
router.register('users', users_viewsets.UserViewSet)
router.register('movies', movies_viewsets.MovieViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtian_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
