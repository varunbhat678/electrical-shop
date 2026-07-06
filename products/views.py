from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


def home(request):
    search = request.GET.get('search', '')

    products = Product.objects.all()

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(brand__icontains=search) |
            Q(category__icontains=search)
        )

    categories = {}

    for product in products:
        categories.setdefault(product.category, []).append(product)

    return render(request, 'home.html', {
        'categories': categories,
        'search': search
    })


def category(request, category_name):
    products = Product.objects.filter(category=category_name)

    return render(request, 'category.html', {
        'products': products,
        'category': category_name
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'product_detail.html', {
        'product': product
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')