from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ClienteForm, PaisForm
from .models import Cliente, Pais


@login_required
def index(request):
    return render(request, 'clientes/index.html')


def pais_list(request):
    q = request.GET.get('q')
    if q:
        query = Pais.objects.filter(nombre__icontains=q)
    else:
        query = Pais.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/pais_list.html', context)


def pais_create(request):
    if request.method == 'GET':
        form = PaisForm()

    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('clientes:pais_list')

    return render(request, 'clientes/pais_form.html', {'form': form})


def pais_detail(request, pk: int):
    query = Pais.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'clientes/pais_detail.html', context)

#Cliente list

def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/cliente_list.html', context)

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    # template_name = 'productos/productocategoria_list.html'
    # context_object_name = 'categorias'
    # queryset = ProductoCategoria.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Cliente.objects.filter(nombre__icontains=q)
        return queryset


#Cliente create

def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')

    return render(request, 'clientes/cliente_form.html', {'form': form})

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

#Cliente detail

def cliente_detail(request, pk: int):
    query = Cliente.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'clientes/cliente_detail.html', context)

class ClienteDetail(DetailView):
    model = Cliente
    
#Cliente update

def cliente_update(request, pk: int):
    query = Cliente.objects.get(id=pk)
    if request.method == 'GET':
        form = ClienteForm(instance=query)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')

    return render(request, 'clientes/cliente_form.html', {'form': form})


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

#Cliente delete

def cliente_delete(request, pk: int):
    query = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('clientes:cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'object': query})


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')
