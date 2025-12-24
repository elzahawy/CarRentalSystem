from django.contrib import admin
from .models import Vehicle, Booking, Payment

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day', 'is_available')
    list_filter = ('is_available', 'brand')
    search_fields = ('brand', 'model')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'start_date', 'end_date', 'total_price', 'status')
    list_filter = ('status', 'start_date')
    search_fields = ('user__username', 'vehicle__brand')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'method', 'payment_date')
    list_filter = ('method', 'payment_date')
