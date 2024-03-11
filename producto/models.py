from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    descripcion = RichTextField(null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
