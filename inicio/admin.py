from django.contrib import admin
from .models import Monitor, Procesador, Placa

admin.site.register(Procesador)
admin.site.register(Placa)
admin.site.register(Monitor)