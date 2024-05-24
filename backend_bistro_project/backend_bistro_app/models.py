from datetime import datetime, timedelta, time
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Allergen(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    item = models.TextField(max_length=100)
    category = models.TextField(max_length=100)
    spice = models.SmallIntegerField(default=0)
    allergens = models.ManyToManyField(Allergen)

    def __str__(self):
        return self.item


class Customer(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=12)

    def __str__(self):
        return self.name
    


class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dine_in = models.BooleanField(default=True)
    pickup_time = models.TimeField()
    order_item_2 = models.ManyToManyField(MenuItem, through='OrderItem')
    paid = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    dine_status = 'Dine in'    
    if dine_in == False:
        dine_status = f'Takeout - {pickup_time}'

    def __str__(self):
        return f'{self.customer} - {self.dine_status}'


class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='order_item')

    def __str__(self):
        return f'{self.quantity} orders of {self.item}'