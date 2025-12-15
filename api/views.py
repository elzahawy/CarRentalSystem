from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from .models import Vehicle, Booking, Payment
from .serializers import (
    UserSerializer, VehicleSerializer, BookingSerializer,
    PaymentSerializer, RegisterSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response

# -----------------------
# AUTHENTICATION
# -----------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# -----------------------
# USERS
# -----------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# -----------------------
# VEHICLES (Admin-only CRUD)
# -----------------------
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  # Public
        return [permissions.IsAdminUser()]  # Admin-only CRUD

# -----------------------
# BOOKINGS
# -----------------------
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}


# -----------------------
# PAYMENTS
# -----------------------
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']