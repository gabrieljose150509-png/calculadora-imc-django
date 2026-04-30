from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
    path('calc1/', views.pagina1, name='pagina1'),
    path('calc2/', views.pagina3, name='teste pagina'),
    path('conversortemp/', views.conversor_graus_kelvin, name='conversor de graus para kelvin')
]