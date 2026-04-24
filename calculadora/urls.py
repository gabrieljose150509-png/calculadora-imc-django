from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
]