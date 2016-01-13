from django.contrib import admin
from .models import Receita,UnidadeMedida,Ingrediente,Categoria


admin.site.register(Receita)
admin.site.register(UnidadeMedida)
admin.site.register(Ingrediente)
admin.site.register(Categoria)

