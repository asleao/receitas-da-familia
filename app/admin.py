from django.contrib import admin
from .models import Receita,UnidadeMedida,Ingrediente,Categoria,Produto,IngredienteQuantidade


admin.site.register(Receita)
admin.site.register(UnidadeMedida)
admin.site.register(Produto)
admin.site.register(Ingrediente)
admin.site.register(IngredienteQuantidade)
admin.site.register(Categoria)

