from django.db.models import Avg
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import SupplierForm, ClientForm, OrderForm, ManagerForm, CommentForm
from .models import Clients, Suppliers, Order, Manager, Comment


def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'base/index.html', data)


# _Client_
def clients(request):
    client = Clients.objects.all()
    return render(request, 'base/clients.html', {'clients': client})


class ClDetailView(DetailView):
    model = Clients
    template_name = 'base/client_details_view.html'
    context_object_name = 'client'


class ClUpdateView(UpdateView):
    model = Clients
    template_name = 'base/client_create.html'
    form_class = ClientForm


class ClDeleteView(DeleteView):
    model = Clients
    context_object_name = 'client'
    success_url = '/clients'
    template_name = 'base/client_delete.html'


def ClCreate(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
        else:
            error = 'Неверная форма'
    form = ClientForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/client_create.html', data)


# _Supplier_
def suppliers(request):
    supplier = Suppliers.objects.all()
    return render(request, 'base/suppliers.html', {'suppliers': supplier})


class SupDetailView(DetailView):
    model = Suppliers
    template_name = 'base/supplier_details_view.html'
    context_object_name = 'supplier'


class SupUpdateView(UpdateView):
    model = Suppliers
    template_name = 'base/supplier_create.html'
    form_class = SupplierForm


class SupDeleteView(DeleteView):
    model = Suppliers
    context_object_name = 'supplier'
    success_url = '/suppliers'
    template_name = 'base/supplier_delete.html'

def SupCreate(request):
    error = ''
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
        else:
            error = 'Неверная форма'
    form = SupplierForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/supplier_create.html', data)


# _Order_
def orders(request, filter):
    ord = Order.objects.order_by(filter)
    avg = Order.objects.all().aggregate(Avg('price'))
    avg = round(avg['price__avg'])
    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            nord = Order.objects.filter(Q(name__icontains=search) | Q(date__icontains=search))
            return render(request, 'base/orders.html', {'orders': nord, 'search': search})
    return render(request, 'base/orders.html', {'orders': ord, 'avg': avg})


class OrdDetailView(DetailView):
    model = Order
    template_name = 'base/order_details_view.html'
    context_object_name = 'order'


class OrdUpdateView(UpdateView):
    model = Order
    template_name = 'base/order_create.html'
    form_class = OrderForm


class OrdDeleteView(DeleteView):
    model = Order
    context_object_name = 'order'
    success_url = '/orders_search/-date'
    template_name = 'base/order_delete.html'


def OrdCreate(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders', filter='-date')
        else:
            error = 'Неверная форма'
    form = OrderForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/order_create.html', data)


# _Manager_
def managers(request):
    man = Manager.objects.all()
    return render(request, 'base/managers.html', {'managers': man})


class ManDetailView(DetailView):
    model = Manager
    template_name = 'base/manager_details_view.html'
    context_object_name = 'manager'


class ManUpdateView(UpdateView):
    model = Manager
    template_name = 'base/order_create.html'
    form_class = ManagerForm


class ManDeleteView(DeleteView):
    model = Manager
    context_object_name = 'manager'
    success_url = '/managers'
    template_name = 'base/manager_delete.html'


def ManCreate(request):
    error = ''
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('managers')
        else:
            error = 'Неверная форма'
    form = ManagerForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/manager_create.html', data)


# _____Comments______
def comment_new(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.client = client
            comment.save()
            return redirect('/clients/%s' % client_id)
    else:
        form = CommentForm()
    return render(request, 'base/comment_edit.html', {'form': form})


def comment_edit(request, client_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/clients/%s' % client_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'base/comment_edit.html', {'form': form})


def comment_remove(request, client_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('/clients/%s' % client_id)


def documents(request):
    return render(request, 'base/documents.html')