from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.lista_agendamentos, name="lista_agendamentos"),
    path('agendamentos/novo', views.cadastro_agendamentos, name="cadastro_agendamentos"),
    path('', views.total_agendamentos, name='home'),
]