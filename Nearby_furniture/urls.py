from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('', include('home.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    # path('', include('products.urls')),
]
