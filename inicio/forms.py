from django import forms
from ckeditor.fields import RichTextFormField


class FormularioBaseAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    biografia = RichTextFormField()


class FormularioCreacionAlumno(FormularioBaseAlumno):
    ...


class FormularioEdicionAlumno(FormularioBaseAlumno):
    nota = forms.IntegerField()


class FormularioBusquedaAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
