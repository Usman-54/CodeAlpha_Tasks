from django.db import transaction
from django.utils import timezone
from .models import InventoryItem, Order, OrderItem, Reservation, Table
from decimal import Decimal


class InsufficientStock(Exception):
    pass


def is_table_available(table, start, end):
    from django.db.models import Q
    return not Reservation.objects.filter(
        table=table,
        start_time__lt=end,
        end_time__gt=start
    ).exists()


@transaction.atomic
def process_order(order_data, items_data):
    table = order_data.get("table")
    now = timezone.now()

    # If table is used, check availability
    if table:
        if not is_table_available(table, now, now):
            raise Exception("Table is not available.")

    order = Order.objects.create(customer_name=order_data["customer_name"], table=table)

    total = Decimal("0.00")

    for item in items_data:
        menu_item = item["menu_item"]
        qty = item["quantity"]

        inv = InventoryItem.objects.select_for_update().get(menu_item=menu_item)

        if inv.quantity < qty:
            raise InsufficientStock(f"{menu_item.name} out of stock")

        inv.quantity -= qty
        inv.save()

        order_item = OrderItem.objects.create(
            order=order,
            menu_item=menu_item,
            quantity=qty,
            unit_price=menu_item.price
        )

        total += order_item.line_total()

    order.total_price = total
    order.status = "CONFIRMED"
    order.save()

    return order
