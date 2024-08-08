from django.shortcuts import render
from products.models import Products


# Create your views here.

def product_show(request):
    return render(request, "products.html", {'all_products': Products.objects.all()})
