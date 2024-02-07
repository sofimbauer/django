from datetime import datetime
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.template import Template, Context, loader
from inicio.models import Alumno
from inicio.forms import FormularioCreacionAlumno


def inicio(request):
    # v1 - inicial
    # archivo_abierto = open(
    #    r'C:\Users\User\OneDrive\Escritorio\django\templates\inicio.html', 'r'
    # )
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    # dicc = {
    #     'nombre': 'Carlos',
    #     'apellido': 'Perez'
    # }
    # contexto = Context(dicc)
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)

    # v2 - cargadores
    # template = loader.get_template('inicio.html')
    # dicc = {
    #     'nombre': 'Carlos',
    #     'apellido': 'Perez'
    # }
    # template_renderizado = template.render(dicc)
    # return HttpResponse(template_renderizado)

    # v3 - render
    return render(request, 'inicio.html')


def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})


def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Esta es la fecha y hora actual: {fecha}')


def saludo(request, nombre, apellido):
    nombre_forma = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f'Bienvenido {nombre_forma} {apellido_formateado}')


# def crear_alumno(request, nombre, apellido, edad):
#     alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad,
#                     nota=random.randint(1, 10))
#     alumno.save()
#     return render(request, 'crear_alumno.html', {'alumno': alumno})

def crear_alumno(request):
    # v1
    # if request.method == 'POST':
    # nombre = request.POST.get('nombre')
    # apellido = request.POST.get('apellido')
    # edad = request.POST.get('edad')
    # alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad,
    #                 nota=random.randint(1, 10))
    # alumno.save()
    # return render(request, 'crear_alumno.html', {})

    formulario = FormularioCreacionAlumno()
    if request.method == 'POST':
        formulario = FormularioCreacionAlumno(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            nota = random.randint(1, 10)
            alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad,
                            nota=nota)
            alumno.save()
            return redirect('alumnos')
    return render(request, 'crear_alumno.html', {'formulario': formulario})
