from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Booking, Menu

class LittleLemonAPITests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="tester", password="StrongPass123!")
        self.client = APIClient()

    def test_menu_list_is_public(self):
        Menu.objects.create(title="Pasta", price="12.50", inventory=10)
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Pasta")

    def test_menu_create_requires_authentication(self):
        response = self.client.post("/api/menu/", {"title": "Pizza", "price": "15.00", "inventory": 5})
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_menu_item(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/menu/", {"title": "Pizza", "price": "15.00", "inventory": 5})
        self.assertEqual(response.status_code, 201)

    def test_booking_api_requires_authentication(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/bookings/", {
            "first_name": "Alex", "reservation_date": date(2026, 11, 1), "reservation_slot": 18
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
