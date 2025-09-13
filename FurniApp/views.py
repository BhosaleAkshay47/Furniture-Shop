from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, CustomerProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import View
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Customer, Product , Cart


# Home page (protected)
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def buy_now(request):
    return render(request, 'buynow.html')

def chair(request):
    return render(request,'chair.html')

class ProductView(View):
  def get(self, request):
     totalitem=0
     chair= Product.objects.filter(category='ch')
     table= Product.objects.filter(category='tb')
     sofa= Product.objects.filter(category='sf')
     
     if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
     return render(request, 'home.html',{'chair':chair,'table':table,'sofa':sofa,'totalitem':totalitem})


class ProductDetailView(View):
    def get(self,request,pk):
       totalitem=0
       product= Product.objects.get(pk=pk)
       item_already_in_cart =False
       if request.user.is_authenticated:
        item_already_in_cart=Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
        if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
       return render(request,'product_details.html',{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem})

def chairs(request, data=None):
    totalitem=0
    if data == None:
        chair = Product.objects.filter(category='ch')
    elif data=='Manyawar' or data=='Fabindia':
        chair = Product.objects.filter(category='ch').filter(brand=data)
    elif data=='below':
        chair=Product.objects.filter(category='ch').filter(discounted_price__lt=500)
    elif data=='above':
        chair=Product.objects.filter(category='ch').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'chairs.html',{'chair':chair,'totalitem':totalitem})


def sofa(request, data=None):
    totalitem=0
    if data == None:
        sofa = Product.objects.filter(category='sf')
    elif data=='Manyawar' or data=='Fabindia':
        sofa = Product.objects.filter(category='sf').filter(brand=data)
    elif data=='Peter_England' or data=='Nykaa_Fashion':
        sofa = Product.objects.filter(category='sf').filter(brand=data)
    elif data=='below':
        sofa=Product.objects.filter(category='sf').filter(discounted_price__lt=1000)
    elif data=='above':
        sofa=Product.objects.filter(category='sf').filter(discounted_price__gt=1000)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'sofa.html',{'sofa':sofa,'totalitem':totalitem})

def show_cart(request):
 if request.user.is_authenticated:
     totalitem=0
     user=request.user
     cart=Cart.objects.filter(user=user)
     #print(cart)
     amount=0.0
     shipping_amount=70.0
     totalamount=0.0
     cart_product=[p for p in Cart.objects.all() if p.user==user]
     #print(cart_product)
     if request.user.is_authenticated:
      totalitem= len(Cart.objects.filter(user=request.user))
     if cart_product:
         for p in cart_product:
             tempamount=(p.quantity * p.product.discounted_price)
             amount+=tempamount
             totalamount=amount+shipping_amount
         return render(request, 'addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount,'shipping_amount':shipping_amount,'totalitem':totalitem})
     else:
         return render(request,'emptycart.html')    


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            messages.success(request, "Account is created successfully")    
            return redirect('login')
    else:
        initial_data = {'username': '', 'email': '', 'password1': '', 'password2': ''}
        form = SignupForm(initial=initial_data)
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid credentials")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')

def Profile_view(request):
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
    else:
        form = CustomerProfileForm()
    return render(request, 'profile.html', {'form': form})

def address(request):
 totalitem=0
 add =Customer.objects.filter(user=request.user)
 if request.user.is_authenticated:
    totalitem=len(Customer.objects.filter(user=request.user))
    return render(request, 'address.html',{'add':add,'active':'btn-warning','totalitem':totalitem})


def cart_view(request):
    return render(request, 'cart.html')