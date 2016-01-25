from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import ReceitaSerializer,IngredienteSerializer,CategoriaSerializer,UserSerializer
from .models import Receita,Categoria
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate



class ReceitaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                                IsOwnerOrReadOnly,)
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class ReceitaInCategoria(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)    
    serializer_class = ReceitaSerializer
    
    def get_queryset(self):       
        categoria = self.kwargs['pk']
        return Receita.objects.filter(categoria_id=categoria).order_by('id')    

class CategoriaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UserList(generics.ListCreateAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsReceitaOwner(),)     


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer