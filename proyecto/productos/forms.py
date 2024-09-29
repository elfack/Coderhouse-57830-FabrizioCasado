from django import forms
from django.core.exceptions import ValidationError
from django.db import  models
from django.core.validators import RegexValidator
from .models import ProductoCategoria, Pedido, Cliente, Producto


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria #ProductoCategoria
        # fields = ['nombre', 'descripcion']
        fields = '__all__'

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')


        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidationError(
                'El nombre debe tener una longitud mínima de 3 letras o máxima de 50'
            )
        return nombre

#Agregado para Pedidos
   
class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), empty_label="Seleccione un cliente",
    )
    producto = forms.ModelChoiceField(
        queryset=ProductoCategoria.objects.filter(disponible=True),
        empty_label="Seleccione un producto",
        )
    
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {"fecha_entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})}

class CompraForm(forms.ModelForm):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=15,
        null = True,
        blank = False,
        validators=[
            RegexValidator(r'^\d{10,15}$', 'El número de teléfono debe contener solo números (entre 10 y 15 dígitos).')
        ]
       )
    
    class Meta:
        model = Cliente
        fields = '__all__'
    
    producto = forms.ModelChoiceField(
        queryset=ProductoCategoria.objects.filter(disponible=True),
        empty_label="Seleccione un producto",
        )