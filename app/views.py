from django.shortcuts import render
from rest_framework import generics
from serializers import ReceitaSerializer,IngredienteQuantidadeSerializer
from models import Receita,IngredienteQuantidade


class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer    

class ReceitaIngredientesList(generics.ListCreateAPIView):
    queryset = IngredienteQuantidade.objects.all()
    serializer_class = IngredienteQuantidadeSerializer


class ReceitaIngredientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IngredienteQuantidade.objects.all()
    serializer_class = IngredienteQuantidadeSerializer 