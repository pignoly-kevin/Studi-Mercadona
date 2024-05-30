from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Promotion
from .forms import ProductForm, PromotionForm

def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        products = products.filter(category__id=selected_category)
    return render(request, 'store/catalog.html', {'products': products, 'categories': categories})

@login_required
def add_product(request):
    if not request.user.is_staff:
        return redirect('catalog')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

@login_required
def add_promotion(request, product_id):
    if not request.user.is_staff:
        return redirect('catalog')
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.product = product
            promotion.save()
            return redirect('catalog')
    else:
        form = PromotionForm()
    return render(request, 'store/add_promotion.html', {'form': form, 'product': product})
