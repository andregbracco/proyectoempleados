# Generated by Django 3.1 on 2020-09-03 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
