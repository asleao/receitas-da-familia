from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Receita,UnidadeMedida,Ingrediente,Categoria,Produto,IngredienteQuantidade

class UserSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(many=True, queryset=Receita.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'usuario')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = ('id', 'descricao')

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome')

class IngredienteSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()        

    class Meta:
        model = Ingrediente
        fields = ('id', 'produto')      

class ReceitaSerializer(serializers.ModelSerializer):    
    autor = UserSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Receita
        fields = ('id', 'autor','nome','categoria','dataCriacao','modoPreparo',
                          'tempoPreparo','rendimento','grauDificuldade','nota')

class IngredienteQuantidadeSerializer(serializers.ModelSerializer):    
    receita = ReceitaSerializer()
    ingrediente = IngredienteSerializer()
    unidadeMedida = UnidadeMedidaSerializer()

    class Meta:
        model = IngredienteQuantidade
        fields = ('id', 'receita','ingrediente','quantidade','unidadeMedida')
