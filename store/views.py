from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def get(request):
    busqueda = request.GET.get('busqueda')
    result = Product.objects.filter(name=busqueda)
    mensaje = "El resultado es: %s" %result[0]
    return HttpResponse(mensaje)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)