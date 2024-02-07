from django.contrib import admin
from inicio.models import Alumno

# v1
admin.site.register(Alumno)
# admin.site.register(Otro_modelo)

# v2
# admin.site.register(Alumno, Otro_modelo)
