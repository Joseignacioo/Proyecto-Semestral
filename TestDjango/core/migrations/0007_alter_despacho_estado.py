# Generated by Django 4.0.4 on 2022-06-25 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_despacho_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despacho',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='Estado del Despacho'),
        ),
    ]
