from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import ListView

def product_list(request, category_slug=None):
    category = None
    # lấy tất cả các giỏ hàng
    categories = Category.objects.all()
    #chỉ hiện những product còn hàng
    products = Product.objects.filter(available=True)
    # nếu truy cập vào từng cate thì lọc ra các sản phẩm của cate đó
    if category_slug :
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)  
    #  phân trang 12 sản phẩm /1 page
    paginator = Paginator(products, 12)
    pageNumber = request.GET.get('page')
    try:
        products = paginator.page(pageNumber)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'category': category,
                'categories': categories,
                'products': products}                        
    return render(request,'shop/product/list.html', context)


def product_detail(request, id, slug): 
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form })


    