from django.db import models

# Create your models here.

class CategoriaProducto (models.Model):
    idcategoriaP = models.AutoField(primary_key= True)
    descripcionP = models.CharField(max_length= 100)

    def __str__ (self):
        return self.descripcionP

class producto (models.Model):
    idproducto = models.AutoField(primary_key= True)
    nombreproducto = models.CharField(max_length= 150)
    precio = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="IMG/Productos")

    def __str__ (self):
        return self.nombreproducto