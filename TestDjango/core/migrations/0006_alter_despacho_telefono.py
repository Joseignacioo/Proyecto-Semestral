# Generated by Django 4.0.4 on 2022-06-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_estado_despacho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despacho',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
