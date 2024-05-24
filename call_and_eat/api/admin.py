from django.contrib import admin
from .models import CategoriaPlato,Cesta,Categorias, Plato, MenuSemanal, ImagenesPlatos, ImagenCarrusel, InfUbicacion, PagoFinal, InfPlato, Alergenos

admin.site.register(ImagenCarrusel)
admin.site.register(Plato)
admin.site.register(InfUbicacion)
admin.site.register(PagoFinal)
admin.site.register(InfPlato)
admin.site.register(ImagenesPlatos)
admin.site.register(Alergenos)
admin.site.register(Categorias)
admin.site.register(MenuSemanal)  
admin.site.register(Cesta)
admin.site.register(CategoriaPlato)
