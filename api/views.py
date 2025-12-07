from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Vehicle, Booking, Payment
from .serializers import UserSerializer, VehicleSerializer, BookingSerializer, PaymentSerializer

# USERS
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# VEHICLES
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# BOOKINGS
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# PAYMENTS
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Create your views here.
