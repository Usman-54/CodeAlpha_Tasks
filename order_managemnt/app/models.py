from django.db import models
from decimal import Decimal


class MenuItem(models.Model):
    name = models.CharField(max_length=200, default='unnamed')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    menu_item = models.OneToOneField(MenuItem, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.menu_item.name} ({self.quantity})"


class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField(default=4)

    def __str__(self):
        return f"Table {self.number}"





class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=200, default='Anonymous')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    party_size = models.IntegerField()


    def __str__(self):
        return f"{self.name} - {self.table.number}"


class Order(models.Model):
    STATUS = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.unit_price * self.quantity
