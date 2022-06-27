from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('login/',views.login,name='login'),
    path('plataforma/',views.plataforma,name='plataforma'),
    path('cadastro_livros/',views.cadastro_livros,name='cadastro_livros'),
]
