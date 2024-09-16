from django.db import models

# Create your models here.

# class Cliente(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, unique=True, default=None)
#     celular = models.CharField(max_length=15, blank=True, null=True)
#     domicilio = models.CharField(max_length=200, blank=True, null=True)
    
#     def __str__(self):
#         return f'{self.nombre} {self.apellido} {self.celular}'
    
# class Producto(models.Model):
#     nombre = models.CharField(max_length=50, unique=True)
#     descripcion = models.TextField(blank=True, null=True)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     disponible = models.BooleanField(default=True)
    
#     def __str__(self) -> str:
#         return f"{self.nombre}"

# class Pedido(models.Model):
#     class Estado(models.TextChoices):
#         PENDIENTE = 'Pendiente', 'Pendiente'
#         ENTREGADO = 'Entregado', 'Entregado'
#         CANCELADO = 'Cancelado', 'Cancelado'
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     descripcion = models.TextField(blank=True, null=True)
#     fecha_solicitud = models.DateTimeField(auto_now_add=True)
#     fecha_entrega = models.DateTimeField(blank=True, null=True)
#     estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    
#     def __str__(self) -> str:
#         return f"Pedido de {self.producto.nombre} para {self.cliente.apellido}, {self.cliente.nombre}"
    
class ProductoCategoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'


class Producto(models.Model):
    categoria = models.ForeignKey(
        ProductoCategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='categoría',
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    unidad_de_medida = models.CharField(max_length=50, blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        # La siguiente línea es para que no se puedan repetir el nombre y la categoría
        constraints = [
            models.UniqueConstraint(fields=['categoria', 'nombre'], name='categoria_nombre')
        ]
        # La siguiente línea es para crear un índice en la base de datos
        # Un ínidice es una estructura de datos que mejora la velocidad de búsqueda
        indexes = [models.Index(fields=['nombre'])]

    def disminuir_stock(self, cantidad):
        """cantidad es enviado desde el modelo Venta"""
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError('No hay suficiente stock disponible')

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        self.save()
