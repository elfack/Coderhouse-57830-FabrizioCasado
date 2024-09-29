from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'productos'


urlpatterns = [
    path('', views.index, name='index'),
    # path('productocategoria/list', views.productocategoria_list, name='productocategoria_list'),
    path(
        'productocategoria/list',
        views.ProductoCategoriaList.as_view(),
        name='productocategoria_list',
    ),
    
    path('productos', views.productos , name='productos'),
    #path('pedido/list', views.login_ , name='pedido_list'),
    #path('pedido/create', views.pedido_create , name='pedido_create'),
    path('pedido/list', login_required(views.pedido_list), name='pedido_list'),
    path('pedido/create', login_required(views.pedido_create), name='pedido_create'),
    path('comprar', views.comprar, name='pedido_comprar'),
    path('pedido/detail/<int:pk>', login_required(views.PedidoDetail.as_view()), name='pedido_detail'),
    path('pedido/update/<int:pk>', login_required(views.PedidoUpdate.as_view()), name='pedido_update'),
    path('pedido/delete/<int:pk>', login_required(views.PedidoDelete.as_view()), name='pedido_delete'),
    
    
   
    path(
        'productocategoria/create',
        views.ProductoCategoriaCreate.as_view(),
        name='productocategoria_create',
    ),
    path(
        'productocategoria/detail/<int:pk>',
        views.ProductoCategoriaDetail.as_view(),
        name='productocategoria_detail',
    ),
  
    path(
        'productocategoria/update/<int:pk>',
        views.ProductoCategoriaUpdate.as_view(),
        name='productocategoria_update',
    ),
 
    path(
        'productocategoria/delete/<int:pk>',
        views.ProductoCategoriaDelete.as_view(),
        name='productocategoria_delete',
    ),
]
