from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# from django.template import Template, Context, loader


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
    dicc = {
        'nombre': 'Carlos',
        'apellido': 'Perez'
    }
    return render(request, 'inicio.html', dicc)


def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Esta es la fecha y hora actual: {fecha}')


def saludo(request, nombre, apellido):
    nombre_forma = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f'Bienvenido {nombre_forma} {apellido_formateado}')
