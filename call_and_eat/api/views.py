from django.http import JsonResponse
from django.views import View
from django.shortcuts import render  
from django.views.generic import TemplateView
from .models import PagoFinal,Cesta,Categorias, Plato, MenuSemanal, ImagenesPlatos, InfUbicacion 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import json
from .models import ImagenCarrusel

import os

def carrusel_imagenes(request):
    # Ruta a la carpeta donde están almacenadas las imágenes del carrusel
    ruta_carpeta_imagenes = 'D:/2ªDAWRECU/django_mysql_api/img'

    # Obtener la lista de nombres de archivo de todas las imágenes en la carpeta
    nombres_archivos = os.listdir(ruta_carpeta_imagenes)

    # Crear una lista de rutas de archivo completas para las imágenes del carrusel
    rutas_imagenes = [os.path.join(ruta_carpeta_imagenes, nombre_archivo) for nombre_archivo in nombres_archivos]

    # Devolver la lista de rutas de archivo como una respuesta JSON
    return JsonResponse({'imagenes': rutas_imagenes})


class PagPrincipalView(TemplateView):
    template_name = 'pag_principal.html'

class CartaView(View):
    def get(self, request):
        categorias = list(Categorias.objects.values())  
        data = {'message': "Éxito", 'categorias': categorias}
        return JsonResponse(data)

class MenuSemanalView(View):
    def get(self, request):
        # Verificar si el campo 'categoria' está presente en el modelo MenuSemanal
        if hasattr(MenuSemanal, 'categoria'):
            print("El campo 'categoria' está presente en el modelo MenuSemanal")
            # Si el campo 'categoria' está presente, realizar la consulta
            menu_semanal = list(MenuSemanal.objects.values())
            data = {'message': "Éxito", 'menu_semanal': menu_semanal}
            return JsonResponse(data)
        else:
            # Si el campo 'categoria' no está presente, devolver un mensaje de error
            data = {'message': "Error: El campo 'categoria' no está presente en el modelo MenuSemanal"}
            return JsonResponse(data, status=500)


class PlatosCategoriaView(View):
    def get(self, request, categoria_id):
        platos = list(Plato.objects.filter(categoria_id=categoria_id).values())
        data = {'message': "Éxito", 'platos': platos}
        return JsonResponse(data)

class InfPlatoView(View):
    def get(self, request, id):
        try:
            plato = Plato.objects.get(id=id)
            data = {
                "id": plato.id,
                "nombre": plato.nombre,
                "descripcion": plato.descripcion,
                "precio": plato.precio,
                "imagen": plato.imagen.url,
                "alergenos": plato.alergenos,  # Suponiendo que plato.alergenos es una lista de alergenos
            }
            return JsonResponse(data)
        except Plato.DoesNotExist:
            return JsonResponse({'error': 'Plato no encontrado'}, status=404)



class CestaView(View):
    def get(self, request):
        cesta = list(Cesta.objects.values())
        data = {'message': "Éxito", 'cesta': cesta}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Cesta.objects.create(plato_id=jd['plato_id'], cantidad=jd['cantidad'])
        data = {'message': "Éxito"}
        return JsonResponse(data)

    def delete(self, request, id):
        try:
            item = Cesta.objects.get(id=id)
            item.delete()
            data = {'message': "Éxito"}
        except Cesta.DoesNotExist:
            data = {'message': "Elemento no encontrado..."}
        return JsonResponse(data)

@method_decorator(csrf_protect, name='dispatch')
class PagoFinalView(View):
    def get(self, request):
        pagos = list(PagoFinal.objects.values('nombre', 'apellidos', 'tarjeta_credito', 'direccion', 'cvv', 'codigo_postal', 'fecha_caducidad_tarjeta', 'cantidad'))
        data = {'message': "Éxito", 'pagos': pagos}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        nuevo_pago = PagoFinal(
            nombre=jd['nombre'],
            apellidos=jd['apellidos'],
            telefono=jd['telefono'],
            tarjeta_credito=jd['tarjeta'],
            direccion=jd['direccion'],
            cvv=jd['cv'],
            codigo_postal=jd['cp'],
            fecha_caducidad_tarjeta=jd['fecha']
        )
        nuevo_pago.save()
        data = {'message': "Pago guardado con éxito"}
        return JsonResponse(data, status=201)
    
class GaleriaView(View):
    def get(self, request):
        imagenes = list(ImagenesPlatos.objects.values())
        data = {'message': "Éxito", 'imagenes': imagenes}
        return JsonResponse(data)

class PlatosView(View):
    def get(self, request):
        platos = list(Plato.objects.values())
        data = {'message': "Éxito", 'platos': platos}
        return JsonResponse(data)
    
class InfUbicacionView(View):
    def get(self, request):
        # Obtener los datos del modelo InfUbicacion
        ubicacion = InfUbicacion.objects.all().values()  # values() para obtener los datos como diccionarios
        # Convertir QuerySet a lista
        ubicacion_list = list(ubicacion)
        return JsonResponse(ubicacion_list, safe=False)