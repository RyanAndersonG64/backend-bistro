import datetime
from django.db import models

# Create your models here.

class MenuItem():
    item = models.TextField(max_length=100)
    category = models.TextField(max_length=100)
    spice = models.SmallIntegerField(default=0)
    allergens = models.TextField(max_length=100)

class Customer():
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

class CustomerOrder():
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    quantity = models.SmallIntegerField(default=0)
    dine_in = models.BooleanField(default=True)
    pickup_time = models.TimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)
