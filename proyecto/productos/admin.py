# from django.contrib import admin
# from .models import Cliente, Producto, Pedido


# # Register your models here.

# # admin.site.register(Cliente)
# # admin.site.register(Producto)
# # admin.site.register(Pedido)

# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ("apellido", "nombre", "email", "celular", "domicilio")
#     search_fields = ("nombre", "apellido", "email", "celular", "domicilio")
#     ordering = ("apellido", "nombre")

# @admin.register(Producto)
# class ProductoAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "precio", "disponible")
#     list_filter = ("disponible",)
#     search_fields = ("nombre",)
#     ordering = ("nombre",)
    
# @admin.register(Pedido)
# class PedidoAdmin(admin.ModelAdmin):
#     list_display = ("cliente", "producto", "estado", "fecha_solicitud", "fecha_entrega")
#     list_filter = ("estado", "fecha_solicitud")
#     search_fields = ("cliente__nombre", "producto__nombre")
#     ordering = ("fecha_entrega",)
#     date_hierarchy = "fecha_solicitud"


from django.contrib import admin

from .models import Producto, ProductoCategoria

admin.site.register(ProductoCategoria)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'stock', 'unidad_de_medida', 'precio')
    list_filter = ('categoria', 'unidad_de_medida')
    search_fields = ('nombre', 'categoria__nombre')
