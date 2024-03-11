from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from producto.models import Auto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Autos(ListView):
    model = Auto
    context_object_name = 'autos'
    template_name = 'autos/autos.html'

class CrearAuto(CreateView):
    model = Auto
    template_name = 'autos/crear_auto.html'
    fields = ['marca', 'modelo', 'fecha_fabricacion', 'descripcion']
    success_url = reverse_lazy('autos')

class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = 'autos/eliminar_auto.html'
    success_url = reverse_lazy('autos')

class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = 'autos/editar_auto.html'
    success_url = reverse_lazy('autos')
    fields = ['marca', 'modelo', 'fecha_fabricacion', 'descripcion']

class DetalleAuto(DetailView):
    model = Auto
    template_name = 'autos/detalle_auto.html'