from django.shortcuts import render,redirect
from orders.utilities import checkout,notify_customer,notify_vendor
from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm
from .cart import Cart
import stripe



def cartview(request):
    cart = Cart(request)
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']
            try:
                charge = stripe.Charge.create(
                    amount=int(cart.get_total_cost() * 100),
                    currency='USD',
                    description="Charge from JustBuy",
                    source=stripe_token
                )
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = checkout(request, first_name,last_name,email, phone,address,zipcode,place, cart.get_total_cost())

                cart.clear()
                notify_customer(order)
                notify_vendor(order)
                
                return redirect('success')
            except Exception:
                messages.error(request, "Something went wrong with the payment")
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity , True)
        return redirect('cart')
    context = {
        "form":form, 
        "stripe_pub_key": settings.STRIPE_PUB_KEY
        }

    return render(request, 'cart.html', context)

def SuccesView(request):
    return render(request, 'success.html')