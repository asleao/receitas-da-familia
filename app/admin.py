from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Receita)
admin.site.register(models.UnidadeMedida)
admin.site.register(models.Ingrediente)
admin.site.register(models.Categoria)
