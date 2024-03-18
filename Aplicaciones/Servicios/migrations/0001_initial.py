# Generated by Django 4.2.7 on 2023-12-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('Id_producto', models.BigAutoField(primary_key=True, serialize=False)),
                ('TipoBebida', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.FloatField()),
                ('Id_servicio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('Id_producto', models.BigAutoField(primary_key=True, serialize=False)),
                ('TipoPlatillo', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.FloatField()),
                ('Id_servicio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ZonasHumedas',
            fields=[
                ('Id_productoZH', models.BigAutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=40)),
                ('Precio', models.FloatField()),
                ('Id_servicio', models.IntegerField()),
            ],
        ),
    ]
