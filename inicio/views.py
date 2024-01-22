from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from inicio.models import Procesador, Placa, Monitor
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from inicio.forms import CrearMonitorFormulario, BusquedaMonitorFormulario, ActualizarMonitorFormulario


def inicio(request):
    return render(request, 'inicio/inicio.html', {})

# MONITORES

def listado_monitores(request):    
    formulario = BusquedaMonitorFormulario(request.GET)
    listado_de_monitores = None
    
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_monitores = Monitor.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaMonitorFormulario()
    return render(request, 'inicio/monitores.html', {'formulario': formulario, 'listado_de_monitores': listado_de_monitores})

@login_required
def crear_monitor(request):    
    
    if request.method == 'POST':
        formulario = CrearMonitorFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
    
            monitor = Monitor(marca=marca.lower(), descripcion=descripcion, anio=anio)
            monitor.save()
            
            return redirect('monitores')
        else:
            return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})
        
    formulario = CrearMonitorFormulario()
    return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})

@login_required
def eliminar_monitor(request, monitor_id):
    monitor_a_eliminar = Monitor.objects.get(id=monitor_id)
    monitor_a_eliminar.delete()
    return redirect("monitores")

@login_required
def actualizar_monitor(request, monitor_id):
    monitor_a_actualizar = Monitor.objects.get(id=monitor_id)
    
    if request.method == "POST":
        formulario = ActualizarMonitorFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            monitor_a_actualizar.marca = info_nueva.get('marca')
            monitor_a_actualizar.descripcion = info_nueva.get('descripcion')
            monitor_a_actualizar.anio = info_nueva.get('anio')
            
            monitor_a_actualizar.save()
            return redirect('inicio/monitores')
        else:
            return render(request, 'inicio/monitores.html', {'formaulario': formulario})
    
    
    formulario = ActualizarMonitorFormulario(initial={'marca': monitor_a_actualizar.marca, 'descripcion': monitor_a_actualizar.descripcion,'anio': monitor_a_actualizar.anio})
    return render(request, 'inicio/actualizar_monitor.html', {'formulario': formulario})

def detalle_monitor(request, monitor_id):
    monitor = Monitor.objects.get(id=monitor_id)
    return render(request, 'inicio/detalle_monitor.html', {'monitor': monitor})

# PROCESADORES

class ListadoProcesadores(ListView):
    model = Procesador
    context_object_name = 'listado_de_procesadores'
    template_name = 'inicio/procesadores.html'
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            listado_de_procesadores = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_procesadores = self.model.objects.all()
        return listado_de_procesadores    
    
class CrearProcesador(LoginRequiredMixin, CreateView):
    model = Procesador
    template_name = "inicio/crear_procesador.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('procesadores')


class ActualizarProcesador(LoginRequiredMixin, UpdateView):
    model = Procesador
    template_name = "inicio/actualizar_procesador.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('procesadores')


class DetalleProcesador(DetailView):
    model = Procesador
    template_name = "inicio/detalle_procesador.html"


class EliminarProcesador(LoginRequiredMixin, DeleteView):
    model = Procesador
    template_name = "inicio/eliminar_procesador.html"
    success_url = reverse_lazy('procesadores')
    
    
    # PLACAS DE VIDEO  
    
class ListadoPlacas(ListView):
    model = Placa
    context_object_name = 'listado_de_placas'
    template_name = 'inicio/placas.html'
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            listado_de_placas = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_placas = self.model.objects.all()
        return listado_de_placas   
    
class CrearPlaca(LoginRequiredMixin, CreateView):
    model = Placa
    template_name = "inicio/crear_placa.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('placas')


class ActualizarPlaca(LoginRequiredMixin, UpdateView):
    model = Placa
    template_name = "inicio/actualizar_placa.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('placas')


class DetallePlaca(DetailView):
    model = Placa
    template_name = "inicio/detalle_placa.html"


class EliminarPlaca(LoginRequiredMixin, DeleteView):
    model = Placa
    template_name = "inicio/eliminar_placa.html"
    success_url = reverse_lazy('placas')



