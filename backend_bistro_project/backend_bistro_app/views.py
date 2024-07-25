from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets

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

@api_view(['PATCH'])
def check_out(request):
    order = CustomerOrder.objects.get(pk = request.data['order'])

    order.paid = True
    request.data['customer'] = order.customer.pk
    request.data['dine_status'] = order.dine_status
    request.data['pickup_time'] = order.pickup_time

    serialized_order = CustomerOrderSerializer(order, data = request.data)
    if serialized_order.is_valid():
        serialized_order.save()
        return Response(serialized_order.data)
    return Response(serialized_order.errors)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer