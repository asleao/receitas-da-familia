from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import ReceitaSerializer,IngredienteSerializer,CategoriaSerializer,UserSerializer
from .models import Receita,Categoria
from django.contrib.auth.models import User
from rest_framework import permissions



class ReceitaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class CategoriaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer