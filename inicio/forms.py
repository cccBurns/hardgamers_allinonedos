from django import forms
from ckeditor.fields import RichTextFormField
  

class BaseMonitorFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()    
    imagen = forms.ImageField(required=False)
    

class CrearMonitorFormulario(BaseMonitorFormulario):
    ...


class ActualizarMonitorFormulario(BaseMonitorFormulario):
    ...
    
class BusquedaMonitorFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)