from django import forms


class FormularioBaseAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()


class FormularioCreacionAlumno(FormularioBaseAlumno):
    ...


class FormularioEdicionAlumno(FormularioBaseAlumno):
    nota = forms.IntegerField()


class FormularioBusquedaAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
