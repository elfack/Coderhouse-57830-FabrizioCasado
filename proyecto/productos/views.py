from django.shortcuts import render, redirect
from .models import Cliente, Pedido, Producto
from .forms import ProductoForm, PedidoForm, ClienteForm


# Create your views here.

def index(request):
    return render(request, 'productos/index.html')

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, 'productos/cliente_list.html', context)

def producto_list(request):
    query = Producto.objects.all()
    context = {"object_list": query}
    return render(request, 'productos/producto_list.html', context)

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, 'productos/pedido_list.html', context)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    return render(request, 'productos/cliente_create.html', {"form":form})

def producto_create(request):
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    return render(request, 'productos/producto_create.html', {"form": form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    return render(request, 'productos/pedido_create.html', {"form":form})