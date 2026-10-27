from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views
from restaurant.api_views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.book, name="home"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("bookings", views.bookings_api, name="bookings_api_legacy"),
    path("api/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api-auth/", include("rest_framework.urls")),
]
