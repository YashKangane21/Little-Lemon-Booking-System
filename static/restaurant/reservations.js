document.addEventListener("DOMContentLoaded", () => {
  const output = document.getElementById("reservations-json");
  const dateInput = document.getElementById("filter-date");
  const result = document.getElementById("filter-result");

  async function load(url = "/bookings") {
    output.textContent = "Loading...";
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error("Request failed");
      const data = await response.json();
      output.textContent = JSON.stringify(data, null, 2);
      result.textContent = data.length ? `${data.length} reservation(s) found.` : "No Booking";
    } catch (error) {
      output.textContent = "Unable to retrieve reservations.";
    }
  }
  document.getElementById("filter-button").addEventListener("click", () => {
    const date = dateInput.value;
    load(date ? `/bookings?date=${encodeURIComponent(date)}` : "/bookings");
  });
  load();
});
