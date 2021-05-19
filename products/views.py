from django.shortcuts import render, get_object_or_404,redirect
from  .models import Category,Product
import random
from django.contrib import messages
from .forms import AddToCartForm
from cart.cart import Cart


def ProductDetailView(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            
            messages.success(request, 'product added succesfully')
            return redirect('product-detail', category_slug=category_slug, product_slug=product_slug )
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
         similar_products = random.sample(similar_products, 4)

    template_name = 'product_detail.html'
    context = {
        'form':form,
        'product': product,
        'similar_products': similar_products,

        }
    
    return render(request, template_name, context)

def CategoryView(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, "product_category.html", {"category":category})
