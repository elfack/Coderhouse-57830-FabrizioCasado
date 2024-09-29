from django.contrib import admin

from .models import Producto, ProductoCategoria, Pedido

admin.site.register(ProductoCategoria)


# @admin.register(Producto)
# class ProductoAdmin(admin.ModelAdmin):
#     list_display = ('categoria', 'nombre', 'precio')
#     list_filter = ('categoria',)
#     search_fields = ('nombre', 'categoria__nombre')
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("producto", "precio", "disponible")
    list_filter = ("disponible",)
    search_fields = ("producto",)
    ordering = ("producto",)
    
#Agregado para pedidos

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "producto", "estado", "fecha_solicitud", "fecha_entrega")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "servicio__nombre")
    ordering = ("fecha_entrega",)
    date_hierarchy = "fecha_solicitud"
    
