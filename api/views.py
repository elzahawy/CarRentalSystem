from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Min, Max

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
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_201_CREATED
        )



# -----------------------
# USERS (ADMIN ONLY)
# -----------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# -----------------------
# VEHICLES (Public read, Admin write)
# -----------------------
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


# -----------------------
# BOOKINGS
# -----------------------
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin sees all bookings
        if user.is_staff:
            return Booking.objects.all()

        # Users see ONLY their bookings
        return Booking.objects.filter(user=user)


# -----------------------
# PAYMENTS
# -----------------------
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()   # ✅ REQUIRED (fixes router error)
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        user = self.request.user

        # Admin sees all payments
        if user.is_staff:
            return Payment.objects.all()

        # Users see ONLY their payments
        return Payment.objects.filter(booking__user=user)


# -----------------------
# VEHICLE PRICE RANGE (PUBLIC)
# -----------------------
@api_view(['GET'])
def vehicle_price_range(request):
    prices = Vehicle.objects.aggregate(
        cheapest=Min('price_per_day'),
        most_expensive=Max('price_per_day')
    )

    return Response({
        "currency": "USD",
        "cheapest_per_day": prices["cheapest"],
        "most_expensive_per_day": prices["most_expensive"],
    })
