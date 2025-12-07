from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, VehicleViewSet, BookingViewSet, PaymentViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('vehicles', VehicleViewSet)
router.register('bookings', BookingViewSet)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
