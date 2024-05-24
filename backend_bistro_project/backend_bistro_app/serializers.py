from rest_framework import serializers
from .models import *

class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    allergens = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'item', 'category', 'spice', 'allergens']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone_number']

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'customer', 'dine_in', 'pickup_time', 'order_item_2', 'paid', 'complete']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'quantity', 'customer_order']