from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from . import models
from . import permissions


class ReceitaList(generics.ListCreateAPIView):

    queryset = models.Receita.objects.all()
    serializer_class = serializers.ReceitaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Receita.objects.all()
    serializer_class = serializers.ReceitaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReceitaInCategoria(generics.ListAPIView):

    serializer_class = serializers.ReceitaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        categoria = self.kwargs['pk']
        return models.Receita.objects.filter(categoria_id=categoria).order_by('id')


class CategoriaList(generics.ListCreateAPIView):

    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """User the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)
