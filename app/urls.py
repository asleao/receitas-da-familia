from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns 
from app import views

urlpatterns = [
        url(r'^receita/$',views.ReceitaList.as_view()),
        url(r'^receita/(?P<pk>[0-9]+)/$',views.ReceitaDetail.as_view()),
        url(r'^receita/ingredientes/$',views.ReceitaIngredientesList.as_view()),
        url(r'^receita/ingredientes/(?P<pk>[0-9]+)/$',views.ReceitaIngredientesDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)