from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo, crear_alumno, alumnos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mostrar-horario/', mostrar_horario, name='mostrar_horario'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('alumnos/', alumnos, name='alumnos'),
    # path('alumnos/nuevo/<str:nombre>/<str:apellido>/<int:edad>/',
    #      crear_alumno, name='crear_alumno')
    path('alumnos/nuevo/', crear_alumno, name='crear_alumno')
]
