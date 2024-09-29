from django.db import models
from clientes.models import Cliente


class ProductoCategoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'


class Producto(models.Model):
    
    producto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.producto} ${self.precio:.2f}'

        
#Agregados para Pedidos

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        ENTREGADO = 'Entregado', 'Entregado'
        CANCELADO = 'Cancelado', 'Cancelado'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoCategoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    
    def __str__(self) -> str:
        return f"Pedido de {self.producto} para {self.cliente.apellido}, {self.cliente.nombre}"
