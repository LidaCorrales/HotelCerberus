# Generated by Django 4.2.7 on 2024-03-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0008_alter_tipodocumento_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='telefono',
            field=models.BigIntegerField(default=None, null=True),
        ),
    ]