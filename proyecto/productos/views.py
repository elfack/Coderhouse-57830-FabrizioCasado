# from django.shortcuts import render, redirect
# from .models import Cliente, Pedido, Producto
# from .forms import ProductoForm, PedidoForm, ClienteForm


# # Create your views here.

# def index(request):
#     return render(request, 'productos/index.html')

# def cliente_list(request):
#     query = Cliente.objects.all()
#     context = {"object_list": query}
#     return render(request, 'productos/cliente_list.html', context)

# def producto_list(request):
#     query = Producto.objects.all()
#     context = {"object_list": query}
#     return render(request, 'productos/producto_list.html', context)

# def pedido_list(request):
#     query = Pedido.objects.all()
#     context = {"object_list": query}
#     return render(request, 'productos/pedido_list.html', context)

# def cliente_create(request):
#     if request.method == "GET":
#         form = ClienteForm()
#     if request.method == "POST":
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cliente_list')
#     return render(request, 'productos/cliente_create.html', {"form":form})

# def producto_create(request):
#     if request.method == "GET":
#         form = ProductoForm()
#     if request.method == "POST":
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('producto_list')
#     return render(request, 'productos/producto_create.html', {"form": form})

# def pedido_create(request):
#     if request.method == "GET":
#         form = PedidoForm()
#     if request.method == "POST":
#         form = PedidoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pedido_list')
#     return render(request, 'productos/pedido_create.html', {"form":form})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductoCategoriaForm
from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


# ****** LIST
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
    # template_name = 'productos/productocategoria_list.html'
    # context_object_name = 'categorias'
    # queryset = ProductoCategoria.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = ProductoCategoria.objects.filter(nombre__icontains=q)
        return queryset


# ****** CREATE
def productocategoria_create(request):
    if request.method == 'GET':
        form = ProductoCategoriaForm()

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('productos:productocategoria_list')

    return render(request, 'productos/productocategoria_form.html', {'form': form})


class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy('productos:productocategoria_list')


# ****** DETAIL


def productocategoria_detail(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'productos/productocategoria_detail.html', context)


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    # context_object_name = 'object'
    # template_name = 'productos/productocategoria_detail.html'


# ****** UPDATE


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


# ****** DELETE
def productocategoria_delete(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('productos:productocategoria_list')
    return render(request, 'productos/productocategoria_confirm_delete.html', {'object': query})


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy('productos:productocategoria_list')
