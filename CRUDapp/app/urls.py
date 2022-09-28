from django.urls import path;
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('products/', views.product, name='products'),
    path('customer/<str:customer_id>/', views.customer, name='customers'),
    path('customerPage/', views.customerPage, name='customerPage'),
    path('create_order/', views.createOrder, name='create_order' ),
    path('create_customer/', views.createCustomer, name='create_customer' ),
    path('update_order/<str:cus_id>', views.updateOrder, name='update_order'),
    path('update_order/<str:cus_id>', views.updateOrderCus, name='update_order_customer'),
    path('delete_order/<str:order_id>', views.orderDelete, name='deleteorder'),
    path('delete_customer/<str:cus_id>', views.customerDelete, name='delete_customer'),
    path('update_customer/<str:cus_id>', views.customerUpdate, name='update_customer'),
    path('delete_product/<str:product_id>', views.productDelete, name='delete_product'),
    path('create_product/', views.createProduct, name='create_product' ),
]

