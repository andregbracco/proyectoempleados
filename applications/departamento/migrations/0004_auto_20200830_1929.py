# Generated by Django 3.1 on 2020-08-30 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20200825_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]