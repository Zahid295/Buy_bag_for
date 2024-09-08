import logging
from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
from products.models import Product


logger = logging.getLogger(__name__)

def check_db_connection(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
        connection_status = 'Database connection successful'
    except OperationalError:
        connection_status = 'Database connection failed'
    return render(request, 'home/check_db_connection.html', {'connection_status': connection_status})

# def index(request):
#         try:
#             product = Product.objects.first()  # Fetch the first product
#             print(product.image_url)  # Fetch the first 3 products as featured
#             return render(request, 'home/index.html', {'featured_products': featured_products})
#         except Exception as e:
#             logger.error(f"Error fetching featured products: {e}")
#             return render(request, 'home/index.html', {'error_message': 'Unable to load featured products at this time.'})
    # featured_products = Product.objects.all()[:3]
    # return render(request, 'home/index.html', {'featured_products': featured_products})

def index(request):
    # Fetch the first 3 products
    featured_products = Product.objects.all()[:3]
    if not featured_products:
        print("No featured products found.")
    print("Fetched the products")
    return render(request, 'home/index.html', {'featured_products': featured_products})

