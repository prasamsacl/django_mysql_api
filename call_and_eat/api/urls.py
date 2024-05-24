from django.urls import path
from .views import (PagPrincipalView, CartaView, PlatosCategoriaView, InfPlatoView, 
                    MenuSemanalView, CestaView, PagoFinalView, GaleriaView, PlatosView, InfUbicacionView)

urlpatterns = [
    path('api', PagPrincipalView.as_view(), name='pag_principal'),
    path('carta/', CartaView.as_view(), name='carta'),  # Ruta para mostrar la carta
    path('categorias/', CartaView.as_view(), name='categorias'),
    path('categorias/<int:categoria_id>/', PlatosCategoriaView.as_view(), name='platos_categoria'),
    path('platos/', PlatosView.as_view(), name='platos'),
    path('plato/<int:id>/', InfPlatoView.as_view(), name='inf_plato'),
    path('menu-semanal/', MenuSemanalView.as_view(), name='menu_semanal'),
    path('cesta/', CestaView.as_view(), name='cesta'),
    path('cesta/<int:id>/', CestaView.as_view(), name='cesta_detail'),
    path('pago_final/', PagoFinalView.as_view(), name='pago_final'),
    path('galeria/', GaleriaView.as_view(), name='galeria'),
    path('ubicacion/', InfUbicacionView.as_view(), name='inf_ubicacion'),  # Nueva ruta para InfUbicacionView
]
