from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, ShippingAddress

# Create your views here.
@login_required
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    shipping = ShippingAddress.objects.filter(order=order).first()
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'items': items,
        'shipping': shipping,
    })

