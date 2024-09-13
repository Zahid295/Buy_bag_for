from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItems
from .forms import CheckoutForm

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, status='Pending')
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order.status = 'Delivered'
            order.save()
            return redirect('order_confirmation')
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form, 'order': order})

@login_required
def order_confirmation(request):
    order = Order.objects.get(user=request.user, status='Delivered')
    return render(request, 'orders/order_confirmation.html', {'order': order})

