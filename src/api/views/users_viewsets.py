from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from ..serializers.users_serializer import UserSerializer
from ..permissions.owner_or_admin import IsOwnerOrAdmin
from ..permissions.authenticated_or_registration import IsAuthenticatedOrRegistration

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrRegistration, IsOwnerOrAdmin]