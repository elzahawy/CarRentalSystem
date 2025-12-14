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
    permission_classes = [permissions.IsAdminUser]  # Only admins can create/update/delete

# -----------------------
# BOOKINGS
# -----------------------
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom endpoint: GET /bookings/user/
    @action(detail=False, methods=['get'], url_path='user')
    def get_user_bookings(self, request):
        user = request.user
        bookings = Booking.objects.filter(user=user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

# -----------------------
# PAYMENTS
# -----------------------
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
