"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees import views as employees_views
from users import views as users_views
from products import views as products_views
from cart_items import views as cart_views
from payments import views as payments_views
from orders import views as orders_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('employees/', employees_views.employeeList.as_view()),
    # Users Apis
    path('users/edits/', users_views.usersEdits.as_view()),
    path('users/', users_views.UserList.as_view()),
    # products Apis
    path('products/edit/', products_views.ProductsEdits.as_view()),
    path('products/', products_views.ProductsList.as_view()),
    # inventory Apis
    path('products/inventory/edit/',
         products_views.Product_Inventory_Edits.as_view()),
    path('products/inventory', products_views.Product_Inventory_List.as_view()),
    # category Apis
    path('products/category/edit', products_views.Product_Category_Edits.as_view()),
    path('products/category/', products_views.Product_Category_List.as_view()),
    # cart_views Apis
    path('cart_views/', cart_views.cart_items_list.as_view()),
    path('cart_views/edit', cart_views.cart_items_list.as_view()),
    # payments Apis
    path('payments/', payments_views.payments_list.as_view()),
    path('payments/edit', payments_views.paymentsEdits.as_view()),
    # orders_views Apis
    path('orders_views/', orders_views.order_details_list.as_view()),
    path('orders_views/edit', orders_views.order_items_Edits.as_view()),
]
