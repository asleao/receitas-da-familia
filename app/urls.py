from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns 
from app import views

urlpatterns = [
        url(r'^receita/$',views.ReceitaList.as_view()),
        url(r'^receita/(?P<pk>[0-9]+)/$',views.ReceitaDetail.as_view()),       
        url(r'^receita/categoria/(?P<pk>[0-9]+)/$',views.ReceitaInCategoria.as_view()),  
        url(r'^categoria/$',views.CategoriaList.as_view()),
        url(r'^categoria/(?P<pk>[0-9]+)/$',views.CategoriaDetail.as_view()),
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())        
] 

urlpatterns = format_suffix_patterns(urlpatterns)