from rest_framework import serializers
from .models import *

class AllergenSerializer(serializers.Serializer):
    class Meta:
        model = Allergen
        fields = ['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'item', 'category', 'spice', 'allergens']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address']

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'customer', 'item', 'quantity', 'dine_in', 'pickup_time', 'paid', 'complete']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'quantity', 'customer_order']