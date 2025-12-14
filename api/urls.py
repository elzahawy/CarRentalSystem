from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RegisterView, UserViewSet, VehicleViewSet,
    BookingViewSet, PaymentViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# DRF Router for CRUD endpoints
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('vehicles', VehicleViewSet)
router.register('bookings', BookingViewSet)
router.register('payments', PaymentViewSet)

# URL Patterns
urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include all router URLs
    path('', include(router.urls)),
]
