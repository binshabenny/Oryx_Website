from django.shortcuts import render,get_object_or_404
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-priority')[:3]
    return render(request,'index.html', {'products': products})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def product_list(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'products': products, 'category': category})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})
