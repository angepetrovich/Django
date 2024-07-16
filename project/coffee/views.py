from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.

from .models import Category, Dish, Order , OrderUser
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User

def menu(request):
    dishes = Dish.objects.all()
    categories = Category.objects.all()
    return render(request, 'menu.html', {'dishes': dishes, 'categories': categories})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('menu')
    template_name = 'signup.html'

def addOrderToCart(request, dish_id):
 if request.user.is_authenticated: 
        dish = Dish.objects.get(id=dish_id)
        order_pom = Order.objects.create(
            dish=dish,
        )
        try:
            order = OrderUser.objects.get(user=request.user, ordered=False)
            if order.orders.filter(dish=dish).exists():
                order_pom = order.orders.get(dish=dish)
                order_pom.quantity += 1
                order_pom.save()
            else:
              order.orders.add(order_pom)
        except:
            order = OrderUser.objects.create(user=request.user, date=timezone.now())
            order.orders.add(order_pom)
        return redirect("cart")
 else:
  return redirect("menu")
    
def addOrder(request):
    if request.user.is_authenticated:
        order = OrderUser.objects.get(user=request.user, ordered=False)
        order.ordered = True        
        order.date = timezone.now()
        order.save()
        return redirect("orders")
    else:
     return redirect("menu")
    
def cart(request):
    if request.user.is_authenticated:
        try:
            order = OrderUser.objects.get(user=request.user, ordered=False)
        except:
            order = OrderUser.objects.create(user=request.user, date=timezone.now())
        orders = order.orders.all()
        final_price = order.final_price()
        return render(request, 'cart.html', {'orders': orders, 'final_price': final_price})
    else:
        return  redirect('menu')

def orders(request):
    if request.user.is_authenticated:
        orders = OrderUser.objects.filter(user=request.user, ordered=True).order_by('-date')
        return render(request, 'orders.html', {'orders': orders})
    else:
        return redirect('menu')

def remove_from_cart(request, order_item_id):
    if request.user.is_authenticated:
        order = OrderUser.objects.get(user=request.user, ordered=False)
        order_item = order.orders.get(id=order_item_id)
        if order_item:
            order.orders.remove(order_item)
            order_item.delete()
        return redirect("cart")
    else:
        return redirect("menu")

def orderDetails(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(OrderUser, id=order_id)
        orders = order.orders.all()
        return render(request, 'orderDetails.html', {'order': order, 'orders': orders, })
    else:
        return redirect('menu')
    
    
        
    
