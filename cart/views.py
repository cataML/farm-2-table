from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart:cart_view')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:
        item.delete()
    return redirect('cart:cart_view')

def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items}) from django.shortcuts import render

# Create your views here.
