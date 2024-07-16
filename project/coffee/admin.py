from django.contrib import admin
from .models import Dish, Order, Category, OrderUser



# Register your models here.

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(OrderUser)
admin.site.register(Order)
