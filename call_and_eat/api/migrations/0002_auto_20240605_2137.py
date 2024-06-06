from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagofinal',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=10, default=0),
        ),
    ]
