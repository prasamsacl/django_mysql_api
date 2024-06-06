from django.contrib import admin
from .models import Cesta, Plato, MenuSemanal, ImagenCarrusel, InfUbicacion, PagoFinal, InfPlato, Alergeno

# Registra tus modelos aquí
admin.site.register(Cesta)
admin.site.register(Plato)
admin.site.register(MenuSemanal)
admin.site.register(ImagenCarrusel)
admin.site.register(InfUbicacion)
admin.site.register(PagoFinal)
admin.site.register(InfPlato)
admin.site.register(Alergeno)


