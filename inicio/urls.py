from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo, crear_alumno, alumnos, ver_alumno, eliminar_alumno, editar_alumno

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mostrar-horario/', mostrar_horario, name='mostrar_horario'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('alumnos/', alumnos, name='alumnos'),
    path('alumnos/nuevo/', crear_alumno, name='crear_alumno'),
    path('alumnos/<int:id_alumno>/', ver_alumno, name='ver_alumno'),
    path('alumnos/<int:id_alumno>/eliminar/', eliminar_alumno, name='eliminar_alumno'),
    path('alumnos/<int:id_alumno>/editar/', editar_alumno, name='editar_alumno')
    ]
