from django.urls import path
from .views import (PagPrincipalView, CartaView, PlatosCategoriaView, InfPlatoView, 
                    MenuSemanalView, CestaView, PagoFinalView, GaleriaView, PlatosView, InfUbicacionView, carrusel_imagenes)

urlpatterns = [
     # Ruta para la página principal
     path('/', PagPrincipalView.as_view(), name='pag_principal'),
    # Ruta para mostrar la carta
    path('carta/', CartaView.as_view(), name='carta'),  
     # Ruta para mostrar categorías
    path('categorias/', CartaView.as_view(), name='categorias'),
    # Ruta para mostrar platos por categoría específica
    path('categorias/<int:categoria_id>/', PlatosCategoriaView.as_view(), name='platos_categoria'),
     # Ruta para mostrar todos los platos
    path('platos/', PlatosView.as_view(), name='platos'),
    # Ruta para mostrar todos los platos
    path('platos/<int:id>/', InfPlatoView.as_view()),
    # Ruta para mostrar el menú semanal
    path('menu-semanal/', MenuSemanalView.as_view(), name='menu_semanal'),
    # Ruta para mostrar la cesta de compras
    path('cesta/', CestaView.as_view(), name='cesta'),
    # Ruta para detalles específicos de la cesta de compras
    path('cesta/<int:id>/', CestaView.as_view(), name='cesta_detail'),
     # Ruta para el pago final
    path('pago_final/', PagoFinalView.as_view(), name='pago_final'),
    # Ruta para la galería de imágenes
    path('galeria/', GaleriaView.as_view(), name='galeria'),
    # Ruta para mostrar información de la ubicación
    path('ubicacion/', InfUbicacionView.as_view(), name='inf_ubicacion'),  
    # Ruta para el carrusel de imágenes
    path('imagen-carrusel/', carrusel_imagenes, name='carrusel_imagenes')

]