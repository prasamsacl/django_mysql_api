from django.db import models
from django.conf import settings

# Defino el modelo para los alérgenos
class Alergeno(models.Model):
    # Campo para el nombre del alérgeno
    nombre = models.CharField(max_length=255)

    def __str__(self):
        # Devuelvo el nombre del alérgeno al convertirlo en cadena
        return self.nombre

# Defino el modelo para las imágenes del carrusel
class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo# Devuelvo el título de la imagen al convertirlo en cadena


# Defino el modelo para las categorías
class Categorias(models.Model):
    imagen = models.ImageField(upload_to='categorias/')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
# Defino el modelo para los platos con la categoria
class Plato(models.Model):
    CATEGORIAS_CHOICES = [
        ('Entrantes', 'Entrantes'),
        ('Caldos y Potajes', 'Caldos y Potajes'),
        ('Patatas y Arroces', 'Patatas y Arroces'),
        ('Carnes', 'Carnes'),
        ('Pastas', 'Pastas'),
        ('Pescado', 'Pescado'),
        ('Postres', 'Postres'),
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    alergenos = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    en_menu_semanal = models.BooleanField(default=False)
    dia_semana = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre
# Defino el modelo para la cesta de compras
#class Cesta(models.Model):
   # plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
   # cantidad = models.IntegerField()
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.plato.nombre} x {self.cantidad}'

from django.db import models

# Defino el modelo para el menú semanal
class MenuSemanal(models.Model):
    PRIMER_PLATO = 'Primer plato'
    SEGUNDO_PLATO = 'Segundo plato'
    POSTRE = 'Postre'
    BEBIDA = 'Bebida'

    CATEGORIAS_CHOICES = [
        (PRIMER_PLATO, 'Primer plato'),
        (SEGUNDO_PLATO, 'Segundo plato'),
        (POSTRE, 'Postre'),
        (BEBIDA, 'Bebida'),
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_categoria_display()}: {self.nombre}"# Devuelvo la categoría y el nombre del plato al convertirlo en cadena


class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    
# Defino el modelo para las opciones de platos en el menú semanal
class OpcionPlato(models.Model):
    menu_semanal = models.ForeignKey(MenuSemanal, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=MenuSemanal.CATEGORIAS_CHOICES)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='menu_semanal/', blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.categoria}: {self.nombre}"

# Defino el modelo para la información de ubicación
class InfUbicacion(models.Model):
    direccion = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    redes_sociales = models.TextField(blank=True)  
    horario = models.TextField(blank=True)

    def __str__(self):
        return self.direccion
# Defino el modelo para el pago final
class PagoFinal(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tarjeta_credito = models.CharField(max_length=16)
    direccion = models.CharField(max_length=255)
    cvv = models.CharField(max_length=4)
    codigo_postal = models.CharField(max_length=10)
    fecha_caducidad_tarjeta = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago: {self.cantidad} - Fecha: {self.fecha}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Almacenar los elementos de la cesta asociados a este pago
        for cesta in self.cesta_set.all():
            cesta.pago_final = self
            cesta.save()

# Defino de nuevo el modelo para la cesta
class Cesta(models.Model):
    # Definir los campos del modelo Cesta
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
   # Defino el modelo para la información del plato 
class InfPlato(models.Model):
    nombre = models.CharField(max_length=255)
    alergenos = models.ManyToManyField(Alergeno)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_alergenos_display()} - {self.descripcion[:50]}"

    def get_alergenos_display(self):
        return ", ".join([alergeno.nombre for alergeno in self.alergenos.all()])

# Defino el modelo para las imágenes de los platos
class ImagenesPlatos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='platos/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Alergenos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre