from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = ('id', 'nome')


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = ('id', 'descricao')


class IngredienteSerializer(serializers.ModelSerializer):
    unidadeMedida = UnidadeMedidaSerializer()

    class Meta:
        model = models.Ingrediente
        fields = ('id', 'nome', 'quantidade', 'unidadeMedida')


class ReceitaSerializer(serializers.ModelSerializer):
    autor = UserProfileSerializer()
    categoria = CategoriaSerializer()
    ingredientes = IngredienteSerializer(many=True)
    tempoPreparo = serializers.TimeField(format='%I:%M')
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = models.Receita
        fields = ('id', 'autor', 'nome', 'categoria', 'dataCriacao', 'ingredientes', 'modoPreparo', 'tempoPreparo', 'rendimento', 'grauDificuldade', 'nota', 'foto')
