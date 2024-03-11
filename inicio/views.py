from datetime import datetime
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.template import Template, Context, loader
from inicio.models import Alumno
from inicio.forms import FormularioCreacionAlumno, FormularioBusquedaAlumno, FormularioEdicionAlumno
from django.contrib.auth.decorators import login_required


def inicio(request):
    # return render(request, 'base.html')
    return render(request, 'inicio/inicio.html')


def alumnos(request):
    formulario = FormularioBusquedaAlumno(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        alumnos = Alumno.objects.filter(nombre__icontains=nombre_a_buscar)
    return render(request, 'inicio/alumnos.html', {'alumnos': alumnos, 'formulario': formulario})


def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Esta es la fecha y hora actual: {fecha}')


def saludo(request, nombre, apellido):
    nombre_forma = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f'Bienvenido {nombre_forma} {apellido_formateado}')


def crear_alumno(request):
    formulario = FormularioCreacionAlumno()
    if request.method == 'POST':
        formulario = FormularioCreacionAlumno(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            biografia = formulario.cleaned_data.get('biografia')
            nota = random.randint(1, 10)
            alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad,
                            biografia=biografia, nota=nota)
            alumno.save()
            return redirect('alumnos')
    return render(request, 'inicio/crear_alumno.html', {'formulario': formulario})

@login_required
def eliminar_alumno(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    alumno.delete()
    return redirect('alumnos')
    # return render(request, 'inicio/eliminar_alumno.html')

@login_required
def editar_alumno(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    formulario = FormularioEdicionAlumno(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'edad': alumno.edad, 'biografia': alumno.biografia, 'nota': alumno.nota})
    if request.method == 'POST':
        formulario = FormularioEdicionAlumno(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            alumno.nombre = info_nueva.get('nombre')
            alumno.apellido = info_nueva.get('apellido')
            alumno.edad = info_nueva.get('edad')
            alumno.biografia = info_nueva.get('biografia')
            alumno.nota = info_nueva.get('nota')
            alumno.save()
            return redirect('alumnos')
    return render(request, 'inicio/editar_alumno.html', {'alumno': alumno, 'formulario': formulario})


def ver_alumno(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    return render(request, 'inicio/ver_alumno.html', {'alumno': alumno})

