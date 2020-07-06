from decimal import Decimal
from django.conf import settings
from shop.models import Product
import decimal


class Cart(object):

    def __init__(self, request):    
# tạo yêu cầu về giỏ hàng
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart :
# save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart



# hàm thêm sản phẩm vào giỏ hàng mặc định là 1
    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        # nếu chưa có sản phẩm id trong giỏ hàng, thì mặc định số lượng bằng 0
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,'price': str(product.price_sale)}
        # update giỏ hàng , mặc định là False
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
# mark the session as "modified" to make sure it gets saved
        self.session.modified = True


# xóa bỏ mặt hàng trong giỏ
    def remove(self, product):      
        product_id = str(product.id)
            # nếu có mặt hàng trong giỏ thì xóa bỏ, gọi phương thức del self.xxx
        if product_id in self.cart:
            del self.cart[product_id]
            # gọi phương thức lưu giỏ hàng ở trên
            self.save()        

        

    def __iter__(self):
         
        product_ids = self.cart.keys()        
# get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

# -----------------------------------------------------------------------------------------------------------
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

# tính tổng đơn hàng
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
# tính đơn hàng cho thành viên
    def get_total_price_user(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()) * decimal.Decimal('0.98')
    
    def clear(self):
    # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()