from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Vendor_Register_Form, ProductForm
from django.utils.text import slugify
from django.contrib.auth import login
from products.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Vendor

# vendor registration
def become_vendor(request):
    if request.method == "POST":
        form  = Vendor_Register_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username , created_by=user)
            return redirect('home')
    else:
        form  = Vendor_Register_Form()

    template_name = 'vendor/become_vendor.html'
    context = {
        "form" : form
    }
    return render(request, template_name, context)

@login_required
def vendor_dashboard(request):
    vendor = request.user.vendor
    orders = vendor.orders.all()
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True
        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    context = {
        "vendor":vendor,
        "orders":orders,
    }
    template_name = "vendor/vendor_dashboard.html"
    return render(request,  template_name,  context)

@login_required
def add_product(request):
    if request.user.vendor:
        if request.method == 'POST':
            form  = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.vendor = request.user.vendor
                product.slug = slugify(product.title)
                product.save()
                messages.success(request, "Product added Successfully")
                return redirect('vendor-dashboard')
        else:
            form  = ProductForm()
    else:
        return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'vendor/vendor_add_product.html', context)

@login_required
def edit_vendor(request):
    vendor = request.user.vendor
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()
        return redirect('vendor-dashboard')

    return render(request, 'vendor/vendor_edit.html', {'vendor':vendor})

@login_required
def vendor_products(request, vendor_id):
    vendor_products = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor/vendor.html', {"vendor_products": vendor_products})




