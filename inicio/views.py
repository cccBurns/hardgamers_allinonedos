from django.shortcuts import render
def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def productos(request):
    
    return render(request, 'inicio/productos.html', {})

