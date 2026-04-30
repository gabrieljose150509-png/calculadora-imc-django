from django.urls import path
from . import views

urlpatterns = [
    path('letras', views.index, name='contar_letras'),
]