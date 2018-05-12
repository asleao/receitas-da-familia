from django.conf.urls import url, include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^receita/$', views.ReceitaList.as_view()),
    url(r'^receita/(?P<pk>[0-9]+)/$', views.ReceitaDetail.as_view()),
    url(r'^receita/categoria/(?P<pk>[0-9]+)/$', views.ReceitaInCategoria.as_view()),
    url(r'^categoria/$', views.CategoriaList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(router.urls))
]
