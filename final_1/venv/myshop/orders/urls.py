from django.urls import path
from . import views
        # itemms 
app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='orders'),
    path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
]