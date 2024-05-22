from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import *
from .serializers import *

# Create your views here.

class AllergenViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer