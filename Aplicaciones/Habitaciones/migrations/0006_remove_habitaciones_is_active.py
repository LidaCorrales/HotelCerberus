# Generated by Django 5.0 on 2024-03-16 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Habitaciones', '0005_habitaciones_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitaciones',
            name='is_active',
        ),
    ]