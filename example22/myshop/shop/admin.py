from django.contrib import admin
from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name', 'category', 'price','available', 'created', 'updated']
    search_fields=[ 'name']
    list_filter = ['category','id']
    list_editable = ['price', 'available','name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product,ProductAdmin)