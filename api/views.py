from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from .models import Vehicle, Booking, Payment
from .serializers import (
    UserSerializer,
    VehicleSerializer,
    BookingSerializer,
    PaymentSerializer,
    RegisterSerializer
)

# -----------------------
# AUTHENTICATION
# -----------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # 

# -----------------------
# USERS (ADMIN ONLY)
# -----------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # ✅ FIXED

# -----------------------
# VEHICLES (Public view, Admin CRUD)
# -----------------------
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  # Public
        return [permissions.IsAdminUser()]  # Admin-only CRUD

# -----------------------
# BOOKINGS (ADMIN ONLY)
# -----------------------
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]  # ✅ Admin only

# -----------------------
# PAYMENTS (ADMIN ONLY)
# -----------------------
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]  # ✅ Admin only
    http_method_names = ['get', 'post']
