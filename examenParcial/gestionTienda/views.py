from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tienda, Producto
from django.urls import reverse


# Create your views here.
def panelNavegacion(request):    
    return render(request,'panelNavegacion.html')

def productos(request):    
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        tienda = request.POST.get('tienda')        
        tiendacod = Tienda.objects.get(id=tienda)
        Producto.objects.create(
            descripcionProducto=descripcion,
            codigoProducto=codigo,
            precioProducto=precio,
            cantidadProducto=cantidad,
            tiendaProducto=tiendacod
        ) 
        return HttpResponseRedirect(reverse('gestionTienda:productos'))
    return render(request,'Producto.html',{
        'productosTotales':Producto.objects.all().order_by('id'),
        'tiendaTotales':Tienda.objects.all().order_by('id')
    
    })

def eliminarProducto(request, idProducto):
    productoEliminar = Producto.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('gestionTienda:productos'))

def eliminarProductoTienda(request, idProducto):   
    productoEliminar = Producto.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('gestionTienda:verProducto'))
    

############################################
def verProducto(request, idTienda):
    tiendaSeleccionado = Tienda.objects.get(id=idTienda)
    productosTienda = tiendaSeleccionado.producto_set.all().order_by('id')
    return render(request,'ProductoTienda.html', {
        'productosTienda':productosTienda,
        'tiendaSeleccionado':tiendaSeleccionado
    })

def asignarProducto(request):
    if request.method == 'POST':
        idProducto = request.POST.get('producto')
        idTienda = request.POST.get('tienda')
        objetoProducto = Producto.objects.get(id=idProducto)
        objectoTienda = Tienda.objects.get(id=idTienda)
        objetoProducto.tiendaProducto = objectoTienda
        objetoProducto.save()
    return HttpResponseRedirect(reverse('gestionTienda:tienda'))

############################################

def tienda(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        provincia = request.POST.get('provincia')
        region = request.POST.get('region')
        fecha = request.POST.get('fecha')
        telefono = request.POST.get('telefono')
        Tienda.objects.create(
            direccionTienda=direccion,
            provinciaTienda=provincia,
            regionTienda=region,
            fechaTienda=fecha,
            telefonoTienda=telefono
        )
        return HttpResponseRedirect(reverse('gestionTienda:tienda'))
    return render(request,'Tienda.html',{
        'productosTotales':Producto.objects.all().order_by('id'),
        'tiendaTotales':Tienda.objects.all().order_by('id')
    })

def eliminarTienda(request,idTienda):
    tiendaEliminar = Tienda.objects.get(id=idTienda)
    tiendaEliminar.delete()
    return HttpResponseRedirect(reverse('gestionTienda:tienda'))


