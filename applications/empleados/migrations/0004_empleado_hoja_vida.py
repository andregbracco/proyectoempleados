# Generated by Django 3.1 on 2020-08-31 00:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_auto_20200830_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
