from django.urls import path
from inicio.views import inicio, productos

urlpatterns = [
    path('', inicio, name='inicio'),        
    path('productos/', productos, name='productos'),
]