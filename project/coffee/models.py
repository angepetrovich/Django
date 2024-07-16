from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return str(self.name)

class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length=200, blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.name) + " " + str(self.price)

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    def final_price(self):
        return self.dish.price * self.quantity

    def __str__(self):
        return str(self.dish) + " " + str(self.quantity)


class OrderUser(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    orders = models.ManyToManyField(Order)
    date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def final_price(self):
        return sum([i.final_price() for i in self.orders.all()])

    def __str__(self):
        return "ID: " + str(self.id) + " " +  self.date.strftime("%d.%m.%Y %H:%M:%S") +  " - " + str(self.user)
