document.addEventListener("DOMContentLoaded", () => {
  const dateInput = document.getElementById("reservation_date");
  const slotSelect = document.getElementById("reservation_slot");
  const list = document.getElementById("booking-list");
  const dateLabel = document.getElementById("booking-date-label");

  async function refreshBookings() {
    const selectedDate = dateInput.value;
    if (!selectedDate) return;
    dateLabel.textContent = selectedDate;
    try {
      const response = await fetch(`/bookings?date=${encodeURIComponent(selectedDate)}`);
      if (!response.ok) throw new Error("Could not load bookings");
      const bookings = await response.json();
      const bookedSlots = new Set(bookings.map(item => String(item.fields.reservation_slot)));
      [...slotSelect.options].forEach(option => {
        if (!option.value) return;
        const isBooked = bookedSlots.has(option.value);
        option.disabled = isBooked;
        option.textContent = option.textContent.replace(" (Booked)", "") + (isBooked ? " (Booked)" : "");
      });
      list.replaceChildren();
      if (bookings.length === 0) {
        const li = document.createElement("li"); li.textContent = "No Booking"; list.appendChild(li);
      } else {
        bookings.forEach(item => {
          const li = document.createElement("li");
          li.textContent = `${item.fields.first_name} - ${Number(item.fields.reservation_slot) > 12 ? Number(item.fields.reservation_slot)-12 + " PM" : item.fields.reservation_slot + (Number(item.fields.reservation_slot) === 12 ? " PM" : " AM")}`;
          list.appendChild(li);
        });
      }
    } catch (error) {
      list.textContent = "Unable to load bookings. Please refresh.";
    }
  }
  dateInput.addEventListener("change", refreshBookings);
  refreshBookings();
});
