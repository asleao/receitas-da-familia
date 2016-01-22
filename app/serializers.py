from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Receita,UnidadeMedida,Ingrediente,Categoria

class UserSerializer(serializers.ModelSerializer):    

    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = ('id', 'descricao')  

class IngredienteSerializer(serializers.ModelSerializer):            
    unidadeMedida =   UnidadeMedidaSerializer() 

    class Meta:
        model = Ingrediente
        fields = ('id', 'nome','quantidade','unidadeMedida')        

class ReceitaSerializer(serializers.ModelSerializer):    
    autor = UserSerializer()
    categoria = CategoriaSerializer()
    ingredientes = IngredienteSerializer(many=True)
    tempoPreparo =  serializers.TimeField(format='%I:%M')   

    class Meta:
        model = Receita
        fields = ('id', 'autor','nome','categoria','dataCriacao','ingredientes','modoPreparo',
                          'tempoPreparo','rendimento','grauDificuldade','nota','foto')


