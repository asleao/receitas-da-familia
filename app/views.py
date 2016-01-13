from django.shortcuts import render
from rest_framework import generics
from serializers import ReceitaSerializer,IngredienteSerializer
from models import Receita,Ingrediente


class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer    

class ReceitaIngredientesList(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class ReceitaIngredientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer 