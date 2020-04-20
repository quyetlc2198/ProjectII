from django.shortcuts import render , redirect ,HttpResponse
from .forms import RegisForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.views import View
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = RegisForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user:login')
    else:
        form = RegisForm()
        return render (request , 'user/reg_form.html', {'form': form} )

def SiteLogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('tendangnhap')
        mat_khau = request.POST.get('password')
        my_user = authenticate(username = user_name , password = mat_khau )
        if my_user is None:
            return render(request , 'user/login.html')
        login(request, my_user)
        return redirect('shop:product_list')
    else:
        return render(request ,'user/login.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('shop:product_list')
    else:
        return redirect('shop:product_list')



