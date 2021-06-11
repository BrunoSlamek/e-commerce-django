from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_usuario, name='login_usuario'),
    path('cadastrar', views.cadastrar_usuario, name='cadastrar_usuario'),
]