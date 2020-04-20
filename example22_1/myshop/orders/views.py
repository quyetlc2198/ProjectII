from django.shortcuts import render, redirect
from .models import OrderItem , Order
from .forms import OrderCreateForm
from django.contrib.auth import authenticate
from cart.cart import Cart
import decimal

def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        total = cart.get_total_price_user()
    else:
        total = cart.get_total_price()


    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.total = total
            order.save()
            for item in cart: 
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            total = order.get_total_cost()
            cart.clear()
            return render(request,'orders/order/created.html',{'order': order})
    else:
        form = OrderCreateForm()
        return render(request,'orders/order/create.html',{'cart': cart, 'form': form})
