from django.urls import path
from producto import views

urlpatterns = [
    path('autos/', views.Autos.as_view(), name='autos'),
    path('autos/nuevo/', views.CrearAuto.as_view(), name='crear_auto'),
    path('autos/<int:pk>/', views.DetalleAuto.as_view(), name='detalle_auto'),
    path('autos/<int:pk>/editar/', views.EditarAuto.as_view(), name='editar_auto'),
    path('autos/<int:pk>/eliminar/', views.EliminarAuto.as_view(), name='eliminar_auto')
]
