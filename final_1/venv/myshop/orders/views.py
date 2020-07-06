from django.shortcuts import render, redirect
from .models import OrderItem , Order
from .forms import OrderCreateForm
from django.contrib.auth import authenticate
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
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


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})
