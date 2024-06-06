
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergeno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenCarrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_carrusel/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InfUbicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='platos/')),
                ('alergenos', models.ManyToManyField(related_name='platos', to='api.Alergeno')),
            ],
        ),
        migrations.CreateModel(
            name='PagoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('tarjeta_credito', models.CharField(max_length=16)),
                ('direccion', models.CharField(max_length=255)),
                ('cvv', models.CharField(max_length=4)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('fecha_caducidad_tarjeta', models.DateField()),
                ('cesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cesta')),
            ],
        ),
        migrations.CreateModel(
            name='MenuSemanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_semana', models.IntegerField()),
                ('platos', models.ManyToManyField(to='api.Plato')),
            ],
        ),
        migrations.CreateModel(
            name='InfPlato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacion', models.TextField()),
                ('plato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.plato')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenPlato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_platos/')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.plato')),
            ],
        ),
        migrations.AddField(
            model_name='cesta',
            name='platos',
            field=models.ManyToManyField(to='api.Plato'),
        ),
    ]
