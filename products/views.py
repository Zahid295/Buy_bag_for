from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product

def all_products(request):
    try:
        products = Product.objects.all()
        if not products:
            return HttpResponse("No products available at the moment.", status=204)
        return render(request, 'products/products.html', {'products': products})
    except Exception as e:
        return HttpResponse("An error occurred while retrieving products.", status=500)

def product_details(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/product_details.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found.")
    except Exception as e:
        return HttpResponse("An error occurred while retrieving product details.", status=500)


