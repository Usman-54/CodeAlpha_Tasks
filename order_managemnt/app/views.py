from rest_framework import generics
from .models import MenuItem, InventoryItem, Table, Reservation, Order
from .serializers import MenuItemSerializer, InventorySerializer, TableSerializer, ReservationSerializer, OrderSerializer

# MenuItem CRUD
class MenuListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Inventory CRUD
class InventoryListCreate(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventorySerializer

class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventorySerializer

# Table CRUD
class TableListCreate(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# Reservation CRUD
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Order CRUD
class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
