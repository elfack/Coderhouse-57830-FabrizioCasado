from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True, default=None)
    celular = models.CharField(max_length=15, blank=True, null=True)
    domicilio = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.celular}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        ENTREGADO = 'Entregado', 'Entregado'
        CANCELADO = 'Cancelado', 'Cancelado'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    
    def __str__(self) -> str:
        return f"Pedido de {self.servicio.nombre} para {self.cliente.apellido}, {self.cliente.nombre}"
    
    