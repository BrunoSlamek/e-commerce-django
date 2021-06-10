from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastrar', views.cadastrar_usuario, name='cadastrar_usuario'),
]