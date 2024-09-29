from django.db import models
from django.core.validators import RegexValidator


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'País de origen'
        verbose_name_plural = 'Países de origen'


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(
        max_length=15,
        null = True,
        blank = False,
        validators=[
            RegexValidator(r'^\d{10,15}$', 'El número de teléfono debe contener solo números (entre 10 y 15 dígitos).')
        ]
    )
    email = models.CharField(max_length=100, null=True, blank=True,)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='País'
    )

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
