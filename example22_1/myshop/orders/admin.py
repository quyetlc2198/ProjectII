from django.contrib import admin
from .models import Order, OrderItem 
from user.models import MyUser


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['name' , 'price', 'quantity']
    # raw_id_fields = ['product']




class OrderAdmin(admin.ModelAdmin):  
    list_display = [ 'first_name', 'address', 'contact', 'note','total', 'created']
    list_filter = [ 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)






    


