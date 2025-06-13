from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from orders.models import Order
from cart.models import Cart  # Or wherever your Cart model is defined
from cart.models import CartItem


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.phone_number = form.cleaned_data['phone_number']
            user.profile.address = form.cleaned_data['address']
            user.profile.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')  
        else:
            print(form.errors)        
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # or redirect('home') if you prefer

 
@login_required
def dashboard_view(request):
    user = request.user
    orders = Order.objects.filter(buyer=user).order_by('-created_at')[:5]
    cart = Cart.objects.filter(user=user).first()
    cart_items_count = cart.items.count() if cart else 0

    saved_items = []  # Optional: implement this if you support saving products/farms

    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
        'cart_items_count': cart_items_count,
        'saved_items': saved_items,
    })

@login_required
def edit_profile(request):
    # Replace with actual form logic
    if request.method == 'POST':
        # Process form data
        pass
    return render(request, 'accounts/edit_profile.html')


