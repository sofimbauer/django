from django.db import models
from django.contrib.auth.models import User

class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f'Datos extra del usuarios {self.user}'
    
