# Generated by Django 5.0.2 on 2024-03-05 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_alter_customuser_numdoc_alter_customuser_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoDocumento',
            fields=[
                ('idTipo', models.IntegerField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='idTipo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacion.tipodocumento'),
        ),
    ]
