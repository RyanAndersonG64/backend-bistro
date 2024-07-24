from rest_framework import serializers
from .models import *

class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    allergens = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.CharField(source = 'item.item', read_only = True)
    item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = OrderItem
        fields = fields = ['id', 'item', 'menu_item', 'quantity', 'customer_order']

        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret['item'] = instance.item.name  # Replace the ID with the name in the representation
            return ret