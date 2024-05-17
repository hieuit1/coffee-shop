from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Coffee, Cart, CartItem
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 


def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

# def home(request):
#     coffee = Coffee.objects.all()
#     return render(request, 'home.html', {'coffee': coffee})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            return HttpResponse("Passwords do not match")
        
        # Kiểm tra xem người dùng đã tồn tại hay không
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return HttpResponseRedirect(reverse('signup'))

        # Tạo người dùng mới
        user = User.objects.create_user(username=username, password=password)
    
        
        messages.success(request, 'Account created successfully. Please log in.')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid username or password.')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'login.html')

def search(request):
    query = request.GET.get('query')
    if query:
        coffee = Coffee.objects.filter(Q(name__icontains=query))
    else:
        coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})



def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, pk=coffee_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, coffee=coffee)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()  # Fetch cart items related to the cart
    return render(request, 'cart.html', {'cart_items': cart_items})


def delete_cart_item(request, item_id):
    
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def about(request):
    return render(request, 'about.html')

def information(request):
    return render(request, 'information.html')