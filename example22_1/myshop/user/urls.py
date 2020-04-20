from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views 

app_name = 'user'

urlpatterns = [
    path('register/', views.register,   name='register1'),
    path('login/' , views.SiteLogin , name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    
]