# Generated by Django 5.0 on 2024-01-26 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='codigo_descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad_recogida', models.CharField(max_length=50)),
                ('ciudad_devolucion', models.CharField(max_length=50)),
                ('fecha_renta', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('codigo_descuento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiculo.codigo_descuento')),
            ],
            options={
                'verbose_name': 'Formulario de renta',
                'verbose_name_plural': 'Formulario de rentas',
                'ordering': ['order', 'fecha_renta'],
            },
        ),
        migrations.CreateModel(
            name='tipo_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vehiculo', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AddField(
            model_name='rent',
            name='tipo_vehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiculo.tipo_vehiculo'),
        ),
    ]
