from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vehicle, Booking, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class VehicleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'year',
            'price_per_day', 'is_available', 'name'
        ]

    def get_name(self, obj):
        return f"{obj.brand} {obj.model}"


class BookingSerializer(serializers.ModelSerializer):
    vehicle_name = serializers.CharField(
        source='vehicle.model', read_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id', 'vehicle', 'vehicle_name',
            'start_date', 'end_date',
            'total_price', 'status'
        ]
        read_only_fields = ['total_price', 'status']

    def create(self, validated_data):
        user = self.context['request'].user
        vehicle = validated_data['vehicle']
        start = validated_data['start_date']
        end = validated_data['end_date']

        days = (end - start).days + 1
        total_price = days * vehicle.price_per_day

        return Booking.objects.create(
            user=user,
            vehicle=vehicle,
            start_date=start,
            end_date=end,
            total_price=total_price,
            status="Confirmed"
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user