from django.http import JsonResponse
from django.views import View
from django.shortcuts import render  
from django.views.generic import TemplateView
from .models import PagoFinal,Cesta,Categorias, Plato, MenuSemanal, ImagenesPlatos, InfUbicacion 

import json

class PagPrincipalView(TemplateView):
   template_name = "pag_principal.html"

class CartaView(View):
    def get(self, request):
        categorias = list(Categorias.objects.values())  
        data = {'message': "Éxito", 'categorias': categorias}
        return JsonResponse(data)

class MenuSemanalView(View):
    def get(self, request):
        menu_semanal = list(MenuSemanal.objects.values())
        data = {'message': "Éxito", 'menu_semanal': menu_semanal}
        return JsonResponse(data)

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
                'message': "Éxito",
                'plato': {
                    'id': plato.id,
                    'name': plato.nombre,
                    'price': plato.precio,
                    'alergenos': plato.alergenos,
                    'description': plato.descripcion
                }
            }
        except Plato.DoesNotExist:
            data = {'message': "Plato no encontrado..."}
        return JsonResponse(data)

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

class PagoFinalView(View):
    def get(self, request):
        pagos = list(PagoFinal.objects.values('nombre', 'apellidos', 'tarjeta_credito', 'direccion', 'cvv', 'codigo_postal', 'fecha_caducidad_tarjeta'))
        data = {'message': "Éxito", 'pagos': pagos}
        return JsonResponse(data)
    
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
        ubicacion = InfUbicacion.objects.all()  # O usa filter() si solo quieres ciertos objetos
        context = {
            'ubicacion': ubicacion
        }
        return render(request, 'ubicacion.html', context)  # Asegúrate de que el template se llame 'ubicacion.html'