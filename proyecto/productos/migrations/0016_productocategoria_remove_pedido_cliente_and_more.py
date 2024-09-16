# Generated by Django 5.1.1 on 2024-09-16 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0015_alter_pedido_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoría de Producto',
                'verbose_name_plural': 'Categorías de Productos',
            },
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='disponible',
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_de_medida',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.productocategoria', verbose_name='categoría'),
        ),
        migrations.AddIndex(
            model_name='producto',
            index=models.Index(fields=['nombre'], name='productos_p_nombre_456643_idx'),
        ),
        migrations.AddConstraint(
            model_name='producto',
            constraint=models.UniqueConstraint(fields=('categoria', 'nombre'), name='categoria_nombre'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
