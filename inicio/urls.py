from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mostrar-horario/', mostrar_horario, name='mostrar_horario'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo')
]
