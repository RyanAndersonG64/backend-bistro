import datetime
from django.db import models

# Create your models here.

class Allergen(models.Model):
    name = models.TextField(max_length=100)

class MenuItem(models.Model):
    item = models.TextField(max_length=100)
    category = models.TextField(max_length=100)
    spice = models.SmallIntegerField(default=0)
    allergens = models.ManyToManyField(Allergen)


class Customer(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dine_in = models.BooleanField(default=True)
    pickup_time = models.TimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)


class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='order_item')
    