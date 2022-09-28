from ast import Delete
from functools import total_ordering
import imp
from multiprocessing import context
from django.shortcuts import render, redirect;
from .models import *;
from .forms import CustomerForm, OrderForm, ProductForm

# Create your views here.

def home(request):
    varOrder = Order.objects.all()
    allcustomers = Customer.objects.all()
    delivered = varOrder.filter(order_status = 'Delivered').count()
    outfordelivery = varOrder.filter(order_status = 'Out for Delivery').count()
    pending = varOrder.filter(order_status = 'Pending').count()
    context = {'customers' : allcustomers, 'delivered': delivered, 'pending' : pending, 'outfordelivery' : outfordelivery, 'varOrder': varOrder}
    return render(request, 'app/dashboard.html', context);

def customerPage(request):
    varOrder = Order.objects.all()
    allcustomers = Customer.objects.all()
    delivered = varOrder.filter(order_status = 'Delivered').count()
    outfordelivery = varOrder.filter(order_status = 'Out for Delivery').count()
    pending = varOrder.filter(order_status = 'Pending').count()
    context = {'allcustomers' : allcustomers, 'delivered': delivered, 'pending' : pending, 'outfordelivery' : outfordelivery, 'varOrder': varOrder}
    return render(request, 'app/customerPage.html', context)

def customer(request, customer_id):
    allcustomers = Customer.objects.all()
    customer = Customer.objects.get(id = customer_id)
    orders = customer.order_set.all()
    total_orders = customer.order_set.count()
    context = {'orders':orders, 'customer':customer, 'allcustomers': allcustomers , 'total_orders': total_orders}
    return render(request, 'app/customer.html', context)
    
def product(request):
    products = Product.objects.all()
    return render(request, 'app/products.html', {'products' : products})

def createOrder(request):
    form = OrderForm(); 
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'create_orderForm' : form}
    return render(request, 'app/create_order.html', context)

def updateOrder(request, cus_id):
    initial = Order.objects.get(id = cus_id)
    form = OrderForm(instance=initial);
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=initial)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'create_orderForm' : form}
    return render(request, 'app/create_order.html', context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'create_customerForm' : form}
    return render(request, 'app/create_customer.html', context)
    

def updateOrderCus(request, cus_id):
    initial = Order.objects.get(id = cus_id)
    form = OrderForm(instance=initial);
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=initial)
        if form.is_valid():
            form.save()
            return redirect('/customer/<str:cus_id>')

    context = {'create_orderForm' : form}
    return render(request, 'app/create_order.html', context)

def orderDelete(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(request.POST)
    if request.method == 'POST':
            order.delete();
            return redirect ('/')
    
    context={'form': form}
    return render(request, 'app/deleteorder.html', context)
    
def customerDelete(request, cus_id):
    customer = Customer.objects.get(id = cus_id);
    if request.method == "POST":
        customer.delete();
        return redirect('/')
    context = {'customer' : customer}
    return render(request, 'app/delete_customer.html', context)

def customerUpdate(request, cus_id):
    
    initial = Customer.objects.get(id = cus_id) 
    form = CustomerForm(instance=initial)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=initial);
        if form.is_valid():
            form.save();
            return redirect('/')

    context = {'form': form, 'customer': customer}
    return render(request, 'app/update_customer.html', context)

def productDelete(request, product_id):
    initial = Product.objects.get(id = product_id)
    form = ProductForm()
    if request.method == 'POST':
        initial.delete()
        return redirect('/')
    return render(request, 'app/delete_product.html') 
   
def createProduct(request):
    form = ProductForm();
    if request.method == "POST":
        form = ProductForm(request.POST);
        if form.is_valid():
            form.save();
            return redirect('/products')
    
    context = {'form': form};
    return render(request, 'app/create_product.html', context)

