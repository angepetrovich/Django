from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('addOrderToCart/<int:dish_id>/', views.addOrderToCart, name='addOrderToCart'),
    path('cart/', views.cart, name='cart'),
    path('addOrder/', views.addOrder, name='addOrder'),
    path('orders/' , views.orders, name='orders'),
    path('remove_from_cart/<int:order_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orderDetails/<int:order_id>/', views.orderDetails, name='orderDetails'),

]
