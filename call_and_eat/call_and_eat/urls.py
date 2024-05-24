from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  # Reemplaza 'api' por el nombre de tu aplicación si es diferente
]
