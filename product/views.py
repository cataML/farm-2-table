from django.shortcuts import render, get_object_or_404
from .models import Product, Category 
from django.core.paginator import Paginator

# Create your views here.
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_list(request):
    category_slug = request.GET.get('category')
    products = Product.objects.all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 6)  # 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'categories': Category.objects.all(),
    }
    return render(request, 'product/product_list.html', context)




