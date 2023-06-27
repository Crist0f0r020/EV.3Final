from django.shortcuts import render
from .models import producto
from .form import ProductoForm

# Create your views here.

def index (request):
    return render(request, 'core/index.html')

def carrito (request):
    return render(request, 'core/carrito.html')

def computador (request):
    return render(request, 'core/computador.html')

def notebook (request):
    return render(request, 'core/notebook.html')

def login (request):
    return render(request, 'core/login.html')

def registro (request):
    return render(request, 'core/registro.html')

def indexadmin (request):
    Productos = producto.objects.all()
    return render(request, 'core/admin/indexadmin.html', {"productoss": Productos})

def save_productos(reques):
    form = ProductoForm
    mensaje = ""
    return render(reques,"core/admin/saveproductos.html", {"form": form,"mensaje": mensaje})
