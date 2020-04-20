from django.contrib import admin
from .models import Category, Product
import decimal

admin.site.site_header = 'Duc Quyet shop'
admin.site.index_title = 'Ẩm thực Tây Bắc'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name', 'category', 'price','price_sale','available']
    search_fields=[ 'name', 'price','category']
    list_filter = ['category','price']
    list_editable = ['price', 'name']
    prepopulated_fields = {'slug': ('name',)}
    fields = (('category','name') , 'price' , 'image' , 'description','slug')
    list_per_page = 20
    actions = ('set_available','set_notavailable','apply_discount1','apply_discount2','apply_default',)  
    # set còn hàng
    def set_available(self, request, queryset):
        queryset.update(available = True)
        self.message_user(request , 'Thành công')
    set_available.short_description = 'Còn hàng'
    # set hết hàng
    def set_notavailable(self, request, queryset):
        queryset.update(available = False)
        self.message_user(request , 'Thành công')
    set_notavailable.short_description = 'Hết hàng'

    # set giảm giá
    def apply_discount1(self, request, queryset):
        for product in queryset:
            product.price_sale = product.price * decimal.Decimal('0.9')
            product.save()
    apply_discount1.short_description = 'Giảm 10%% '
    #
    def apply_discount2(self, request, queryset):
        for product in queryset:
            product.price_sale = product.price * decimal.Decimal('0.8')
            product.save()     
    apply_discount2.short_description = 'Giảm 20%% '

    #đưa về giá mặc định
    def apply_default(self, request, queryset):
        for product in queryset:
            product.price_sale  = product.price
            product.save()
    apply_default.short_description = 'Giá mặc định'
    

admin.site.register(Product,ProductAdmin)