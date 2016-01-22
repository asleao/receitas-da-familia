from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from PIL import Image

class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)    

    def __str__(self):
        return self.nome


class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=20, null=True,unique=True)    

    def __str__(self):
        return self.descricao
           
class Ingrediente(models.Model):       
    nome = models.CharField(max_length=20,null=True)    
    quantidade = models.FloatField(null=True)    
    unidadeMedida=models.ForeignKey(
        UnidadeMedida,
        on_delete=models.CASCADE,
        null=True
        )  

    def __str__(self):
        return self.nome  

class Receita(models.Model):
    autor = models.ForeignKey('auth.User', related_name='usuario')
    nome = models.CharField(max_length=20,unique=True)   
    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True
        )    
    dataCriacao = models.DateTimeField(
            default=timezone.now)     
    ingredientes=models.ManyToManyField(Ingrediente)
    modoPreparo = models.TextField()
    tempoPreparo = models.TimeField()
    rendimento = models.PositiveIntegerField(null=True)   
    grauDificuldade = models.PositiveIntegerField()
    nota = models.PositiveIntegerField(null=True,default=0)
    foto = models.ImageField(upload_to='fotos',null=True)

    def __str__(self):
        return self.nome   

   



        
