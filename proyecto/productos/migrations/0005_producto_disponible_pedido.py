# Generated by Django 5.1 on 2024-09-24 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_cliente_options_alter_pais_options_and_more'),
        ('productos', '0004_producto_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
