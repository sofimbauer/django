from django.db import models
from ckeditor.fields import RichTextField

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nota = models.IntegerField()
    biografia = RichTextField(null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.nota}'
