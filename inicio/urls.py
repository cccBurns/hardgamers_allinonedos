from django.urls import path, include
from inicio.views import inicio, listado_monitores, crear_monitor, eliminar_monitor, actualizar_monitor, detalle_monitor,ListadoProcesadores, CrearProcesador, ActualizarProcesador, EliminarProcesador, DetalleProcesador, ListadoPlacas, CrearPlaca, ActualizarPlaca, EliminarPlaca, DetallePlaca


urlpatterns = [
    path('', inicio, name='inicio'),
    path('monitores/', listado_monitores, name='monitores'),
    path('monitores/crear/', crear_monitor, name='crear_monitor'),
    path('monitores/<int:monitor_id>/', detalle_monitor, name='detalle_monitor'),
    path('monitores/<int:monitor_id>/eliminar/', eliminar_monitor, name='eliminar_monitor'),
    path('monitores/<int:monitor_id>/actualizar/', actualizar_monitor, name='actualizar_monitor'),
    path('procesadores/', ListadoProcesadores.as_view(), name='procesadores'),
    path('procesadores/crear/', CrearProcesador.as_view(), name='crear_procesador'),
    path('procesadores/<int:pk>/', DetalleProcesador.as_view(), name='detalle_procesador'),
    path('procesadores/<int:pk>/actualizar/', ActualizarProcesador.as_view(), name='actualizar_procesador'),
    path('procesadores/<int:pk>/eliminar/', EliminarProcesador.as_view(), name='eliminar_procesador'),
    path('placas/', ListadoPlacas.as_view(), name='placas'),
    path('placas/crear/', CrearPlaca.as_view(), name='crear_placa'),
    path('placas/<int:pk>/', DetallePlaca.as_view(), name='detalle_placa'),
    path('placas/<int:pk>/actualizar/', ActualizarPlaca.as_view(), name='actualizar_placa'),
    path('placas/<int:pk>/eliminar/', EliminarPlaca.as_view(), name='eliminar_placa'),
]