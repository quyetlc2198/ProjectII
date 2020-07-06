from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Order, OrderItem 
from user.models import MyUser
from django.urls import reverse
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['name' , 'price', 'quantity']
    raw_id_fields = ['product']


def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id])))

def tong(obj):
    return Order.get_total_cost(obj);

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ['confirm','paid', 'first_name', 'address', 'contact', 'note',tong, 'created',order_detail]
    list_filter = [ 'confirm','paid','created']
    inlines = [OrderItemInline]
    actions = ('set_confirm','set_paid','set_confirm_default','set_paid_default')  

    def set_confirm(self, request, queryset):
        queryset.update(confirm = True)
        self.message_user(request , 'Thành công')
    set_confirm.short_description = 'Xác nhận'

    def set_paid(self, request, queryset):
        queryset.update(paid = True)
        self.message_user(request , 'Thành công')
    set_paid.short_description = 'Thanh toán'

    def set_confirm_default(self, request, queryset):
        queryset.update(confirm = False)
        self.message_user(request , 'Thành công')
    set_confirm_default.short_description = 'Chưa xác nhận'

    def set_paid_default(self, request, queryset):
        queryset.update(paid = False)
        self.message_user(request , 'Thành công')
    set_paid_default.short_description = 'Chưa thanh toán'




    


