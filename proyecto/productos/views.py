from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductoCategoriaForm, PedidoForm, CompraForm
from .models import ProductoCategoria, Pedido
from clientes.models import Cliente
from clientes.forms import ClienteForm


#def index(request):
#    return render(request, 'productos/index.html')

def productos(request):
    return render(request, 'productos/vista_productos.html')


@login_required
def index(request):
    return render(request, 'clientes/index.html')


#CRUDE de Productos

def productocategoria_list(request):
    q = request.GET.get('q')
    if q:
        query = ProductoCategoria.objects.filter(nombre__icontains=q)
    else:
        query = ProductoCategoria.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/productocategoria_list.html', context)


class ProductoCategoriaList(LoginRequiredMixin, ListView):
    model = ProductoCategoria

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = ProductoCategoria.objects.filter(nombre__icontains=q)
        return queryset


def productocategoria_create(request):
    if request.method == 'GET':
        form = ProductoCategoriaForm()

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:productocategoria_list')

    return render(request, 'productos/productocategoria_form.html', {'form': form})


class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy('productos:productocategoria_list')


def productocategoria_detail(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'productos/productocategoria_detail.html', context)


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria


def productocategoria_update(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductoCategoriaForm(instance=query)

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('productos:productocategoria_list')

    return render(request, 'productos/productocategoria_form.html', {'form': form})


class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy('productos:productocategoria_list')


def productocategoria_delete(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('productos:productocategoria_list')
    return render(request, 'productos/productocategoria_confirm_delete.html', {'object': query})


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy('productos:productocategoria_list')


#CRUDE de Pedidos

def pedido_list(request):
    q = request.GET.get('q')
    if q:
        query = Pedido.objects.filter(nombre__icontains=q)
    else:
        query = Pedido.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/pedido_list.html', context)

class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pedido.objects.filter(nombre__icontains=q)
        return queryset
    
    # query = Pedido.objects.all()
    # context = {"object_list": query}
    # return render(request, 'productos/pedido_list.html', context)


def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
        
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:pedido_list')
        
    return render(request, 'productos/pedido_create.html', {"form":form})

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('productos:pedido_list')

#Pedido detail

def pedido_detail(request, pk: int):
    query = Pedido.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'productos/pedido_detail.html', context)

class PedidoDetail(DetailView):
    model = Pedido
    
#Pedido update

def pedido_update(request, pk: int):
    query = Pedido.objects.get(id=pk)
    if request.method == 'GET':
        form = PedidoForm(instance=query)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('productos:pedido_list')

    return render(request, 'productos/pedido_create.html', {'form': form})


class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'productos/pedido_create.html'
    success_url = reverse_lazy('productos:pedido_list')

#Pedido delete

def pedido_delete(request, pk: int):
    query = Pedido.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('productos:pedido_list')
    return render(request, 'productos/pedido_confirm_delete.html', {'object': query})


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('productos:pedido_list')


#Agregado para Compras

def comprar(request):
    if request.method == "GET":
        form = CompraForm()
        
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data["apellido"]
            telefono = form.cleaned_data["telefono"]
            cliente = Cliente.objects.create(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono
                )
            
            
            producto = form.cleaned_data['producto']
            pedido = Pedido.objects.create(
                 cliente=cliente,
                 producto=producto
            )
            
            
            return redirect('core:index')
        
        
    return render(request, 'productos/comprar.html', {"form":form})