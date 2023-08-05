from django.db import models

# Create your models here.

#Estructura de la tabla
class Tienda(models.Model):    
    direccionTienda = models.CharField(max_length=32, blank = True, null = True)
    provinciaTienda = models.CharField(max_length=32, blank = True, null = True)
    regionTienda = models.CharField(max_length=32, blank = True, null = True)
    fechaTienda = models.CharField(max_length=32, blank = True, null = True)
    telefonoTienda = models.CharField(max_length=32, blank = True, null = True)

class Producto(models.Model):
    descripcionProducto = models.CharField(max_length=32, blank = True, null = True)
    codigoProducto = models.CharField(max_length=32, blank = True, null = True)
    precioProducto = models.CharField(max_length=32, blank = True, null = True)
    cantidadProducto = models.CharField(max_length=32, blank = True, null = True)
    tiendaProducto = models.ForeignKey(Tienda,on_delete=models.SET_NULL,blank=True,null=True)

 

 


