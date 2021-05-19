from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from products.models import Product
from django.contrib import messages
from .forms import User_Register_Form


class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'home'
    paginate_by = 4
    ordering = '-date_added'

def SearchView(request):
    if request.method == 'POST':
        searching = request.POST['searching']
        items = Product.objects.filter(title__contains=searching)
        context = {
            'search':searching,
            'items': items
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', {})


def choose_account_type_view(request):
    return render(request, 'choose_account.html', {})


def normal_user_registration_view(request):
    if request.method == "POST":
        form  = User_Register_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form  = User_Register_Form()

    template_name = 'register.html'
    context = {
        "form" : form
    }
    return render(request, template_name, context)

def user_login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully')
            return redirect('/')
        
        else:
            form = AuthenticationForm(request.POST)
            messages.info(request, 'Wrong username or password')
            return render(request, 'login.html', {'form': form})
            
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def user_logout_view(request):
    logout(request)
    return redirect('login')

        




