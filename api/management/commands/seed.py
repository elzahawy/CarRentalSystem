from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Vehicle


class Command(BaseCommand):
    help = "Seed initial users and vehicles"

    def handle(self, *args, **kwargs):

        # =====================
        # USERS
        # =====================

        users = [
            {
                "username": "admin",
                "email": "admincars@gmail.com",
                "password": "admin123",
                "is_superuser": True,
            },
            {
                "username": "manager",
                "email": "manager@carental.com",
                "password": "manager123",
                "is_superuser": True,
            },
            {
                "username": "aisha",
                "email": "aisha@gmail.com",
                "password": "password123",
                "is_superuser": False,
            },
            {
                "username": "john",
                "email": "john@gmail.com",
                "password": "password123",
                "is_superuser": False,
            },
            {
                "username": "maria",
                "email": "maria@gmail.com",
                "password": "password123",
                "is_superuser": False,
            },
        ]

        for u in users:
            if not User.objects.filter(username=u["username"]).exists():
                if u["is_superuser"]:
                    User.objects.create_superuser(
                        username=u["username"],
                        email=u["email"],
                        password=u["password"],
                    )
                else:
                    User.objects.create_user(
                        username=u["username"],
                        email=u["email"],
                        password=u["password"],
                    )

        # =====================
        # VEHICLES
        # =====================

        vehicles = [
            # Economy
            {
                "brand": "Toyota",
                "model": "Corolla",
                "year": 2022,
                "price_per_day": 40,
                "is_available": True,
            },
            {
                "brand": "Honda",
                "model": "Civic",
                "year": 2023,
                "price_per_day": 45,
                "is_available": True,
            },

            # Luxury
            {
                "brand": "BMW",
                "model": "X5",
                "year": 2023,
                "price_per_day": 120,
                "is_available": True,
            },
            {
                "brand": "Mercedes-Benz",
                "model": "S-Class",
                "year": 2024,
                "price_per_day": 150,
                "is_available": True,
            },

            # Supercars 🔥
            {
                "brand": "Ferrari",
                "model": "488 GTB",
                "year": 2022,
                "price_per_day": 500,
                "is_available": True,
            },
            {
                "brand": "Ferrari",
                "model": "SF90 Stradale",
                "year": 2024,
                "price_per_day": 700,
                "is_available": True,
            },
            {
                "brand": "Lamborghini",
                "model": "Huracán",
                "year": 2023,
                "price_per_day": 650,
                "is_available": True,
            },
            {
                "brand": "Bugatti",
                "model": "Chiron",
                "year": 2023,
                "price_per_day": 1200,
                "is_available": True,
            },
            {
                "brand": "McLaren",
                "model": "720S",
                "year": 2023,
                "price_per_day": 600,
                "is_available": True,
            },
        ]

        for v in vehicles:
            Vehicle.objects.get_or_create(
                brand=v["brand"],
                model=v["model"],
                defaults={
                    "year": v["year"],
                    "price_per_day": v["price_per_day"],
                    "is_available": v["is_available"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Users and supercars seeded successfully!")
        )
