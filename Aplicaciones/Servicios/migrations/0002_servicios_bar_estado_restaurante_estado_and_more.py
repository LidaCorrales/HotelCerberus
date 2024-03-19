# Generated by Django 5.0 on 2024-03-16 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('Id_servicio', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('servicio', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='bar',
            name='Estado',
            field=models.CharField(choices=[('En uso', 'En uso'), ('No se usa', 'No se usa'), ('No hay Stock', 'No hay Stock')], default='En uso', max_length=25),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='Estado',
            field=models.CharField(choices=[('En uso', 'En uso'), ('No se usa', 'No se usa'), ('No hay Stock', 'No hay Stock')], default='En uso', max_length=25),
        ),
        migrations.AddField(
            model_name='zonashumedas',
            name='Estado',
            field=models.CharField(choices=[('En uso', 'En uso'), ('No se usa', 'No se usa'), ('No hay Stock', 'No hay Stock')], default='En uso', max_length=25),
        ),
        migrations.AlterField(
            model_name='bar',
            name='Id_servicio',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Servicios.servicios'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='Id_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Servicios.servicios'),
        ),
        migrations.AlterField(
            model_name='zonashumedas',
            name='Id_servicio',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Servicios.servicios'),
        ),
    ]