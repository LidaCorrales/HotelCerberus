# Generated by Django 5.0 on 2024-03-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0005_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='numdoc',
            field=models.IntegerField(null=True),
        ),
    ]
