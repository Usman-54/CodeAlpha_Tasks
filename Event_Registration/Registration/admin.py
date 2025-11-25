from django.contrib import admin
from .models import Event, registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time', 'end_time', 'capacity')
    search_fields = ('title', 'location')
    list_filter = ('start_time', 'end_time')
    ordering = ('start_time',)


@admin.register(registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at', 'cancelled')
    list_filter = ('cancelled', 'created_at')
    search_fields = ('user__username', 'event__title')
    ordering = ('-created_at',)
