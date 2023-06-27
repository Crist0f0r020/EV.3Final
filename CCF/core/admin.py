from django.contrib import admin
from .models import CategoriaProducto, producto
# Register your models here.


admin.site.register(CategoriaProducto),
admin.site.register(producto)