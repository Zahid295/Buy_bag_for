from django.contrib import admin
from .models import Order
from .models import OrderItems


admin.site.register(Order)
admin.site.register(OrderItems)
