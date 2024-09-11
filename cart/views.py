from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order, OrderItems
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItems.objects.get_or_create(order=order, product=product, price=product.price)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    order = Order.objects.get(user=request.user, status='Pending')
    order_items = order.order_items.all()
    total_price = sum(item.get_total_price() for item in order_items)
    return render(request, 'cart/view_cart.html', {'order_items': order_items, 'total_price': total_price})

@login_required
def update_cart_item(request, item_id):
    order_item = get_object_or_404(OrderItems, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            order_item.quantity = quantity
            order_item.save()
        else:
            order_item.delete()
    return redirect('view_cart')

@login_required
def remove_cart_item(request, item_id):
    order_item = get_object_or_404(OrderItems, id=item_id)
    order_item.delete()
    return redirect('view_cart')
