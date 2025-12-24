from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) (${self.price_per_day}/day)"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.user.username} → {self.vehicle}"


class Payment(models.Model):
    PAYMENT_METHODS = (
        ("CASH", "Cash"),
        ("CARD", "Card"),
    )

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} {self.currency} via {self.method}"


