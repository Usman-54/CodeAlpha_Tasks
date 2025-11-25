from django.urls import path
from .views import (
    MenuListCreate, MenuRetrieveUpdateDestroy,
    InventoryListCreate, InventoryRetrieveUpdateDestroy,
    TableListCreate, TableRetrieveUpdateDestroy,
    ReservationListCreate, ReservationRetrieveUpdateDestroy,
    OrderListCreate, OrderRetrieveUpdateDestroy
)

urlpatterns = [
    # Menu endpoints
    path("menu/", MenuListCreate.as_view(), name="menu-list-create"),
    path("menu/<int:pk>/", MenuRetrieveUpdateDestroy.as_view(), name="menu-detail"),

    # Inventory endpoints
    path("inventory/", InventoryListCreate.as_view(), name="inventory-list-create"),
    path("inventory/<int:pk>/", InventoryRetrieveUpdateDestroy.as_view(), name="inventory-detail"),

    # Table endpoints
    path("tables/", TableListCreate.as_view(), name="table-list-create"),
    path("tables/<int:pk>/", TableRetrieveUpdateDestroy.as_view(), name="table-detail"),

    # Reservation endpoints
    path("reservations/", ReservationListCreate.as_view(), name="reservation-list-create"),
    path("reservations/<int:pk>/", ReservationRetrieveUpdateDestroy.as_view(), name="reservation-detail"),

    # Order endpoints
    path("orders/", OrderListCreate.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderRetrieveUpdateDestroy.as_view(), name="order-detail"),
]
