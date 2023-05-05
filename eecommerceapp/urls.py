from django.urls import path
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from eecommerceapp import views

from .views import login_page,products_table,login_func,add_product,update_product,delete_product,admin_logout,index,register,login,shop,user_register,user_login,add_cart,cart_view,delete_cart,user_logout

urlpatterns=[
    path('login_page/',login_page.as_view()),
    path('login_func/',login_func.as_view()),
    path('products_table/',products_table.as_view()),
    path('add_product/',add_product.as_view()),
    path('update_product/',update_product.as_view()),
    path('delete_product/',delete_product.as_view()),
    path('admin_logout/',admin_logout),
    path('',index.as_view()),
    path('register/',register.as_view()),
    path('login/',login.as_view()),
    path('shop/',shop.as_view()),
    path('user_register/',user_register.as_view()),
    path('user_login/',user_login.as_view()),
    path('cart_view/',cart_view.as_view()),
    path('add_cart/',add_cart.as_view()),
    path('delete_cart/',delete_cart.as_view()),
    path('user_logout/',user_logout),


]