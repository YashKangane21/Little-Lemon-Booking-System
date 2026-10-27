from datetime import date
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from .models import Booking

def book(request):
    today = date.today().isoformat()
    selected_date = request.GET.get("date") or today
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        reservation_date = request.POST.get("reservation_date", "")
        slot_raw = request.POST.get("reservation_slot", "")
        try:
            slot = int(slot_raw)
            if not first_name or slot < 10 or slot > 20:
                raise ValueError
            with transaction.atomic():
                Booking.objects.create(
                    first_name=first_name,
                    reservation_date=reservation_date,
                    reservation_slot=slot,
                )
            return redirect(f"/book/?date={reservation_date}&booked=1")
        except (ValueError, IntegrityError):
            return render(request, "restaurant/book.html", {
                "today": today, "selected_date": reservation_date or today,
                "error": "That time is already booked or the details are invalid.",
                "bookings": Booking.objects.filter(reservation_date=reservation_date),
            })
    bookings = Booking.objects.filter(reservation_date=selected_date)
    return render(request, "restaurant/book.html", {
        "today": today, "selected_date": selected_date,
        "bookings": bookings,
        "success": request.GET.get("booked") == "1",
    })

def reservations(request):
    return render(request, "restaurant/reservations.html")

@require_GET
def bookings_api(request):
    selected_date = request.GET.get("date")
    queryset = Booking.objects.all()
    if selected_date:
        queryset = queryset.filter(reservation_date=selected_date)
    data = [{
        "model": "restaurant.booking",
        "pk": booking.pk,
        "fields": {
            "first_name": booking.first_name,
            "reservation_date": booking.reservation_date.isoformat(),
            "reservation_slot": booking.reservation_slot,
        },
    } for booking in queryset]
    return JsonResponse(data, safe=False)
