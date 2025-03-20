document.addEventListener("DOMContentLoaded", function () {
    const eventTypeToggle = document.getElementById("eventToggle");
    const sortToggle = document.getElementById("sortToggle");
    const createdEventsContainer = document.getElementById("created_events");
    const attendingEventsContainer = document.getElementById("attending_events");
    const upcomingTitle = document.getElementById("upcoming_title");
    const popularTitle = document.getElementById("popular_title");

    eventTypeToggle.addEventListener("change", updateEvents);
    sortToggle.addEventListener("change", function () {
        console.log("Sort Toggle Switched! Checked:", this.checked);

         // toggle switch swaps the bold effect
        if (this.checked) {
            // Popular Events selected, filter based on number of attendees
            popularTitle.classList.add("bold");
            upcomingTitle.classList.remove("bold");
        } else {
            // Upcoming Events selected. filter based on date and time
            upcomingTitle.classList.add("bold");
            popularTitle.classList.remove("bold");
        }

        updateEvents();
    });

   /**
     * Dynamically filters and sorts events based on the selected toggle options.
     * - If "Upcoming" is selected, events are sorted by date, then by time (earliest first).
     * - If "Popular" is selected, events are sorted by attendees (most attendees first).
     */
    function updateEvents() {
        const isCreated = !eventTypeToggle.checked;
        const isUpcoming = !sortToggle.checked;

        console.log("Sorting Mode:", isUpcoming ? "Upcoming" : "Popular");

        let container = isCreated ? createdEventsContainer : attendingEventsContainer;
        let events = Array.from(container.querySelectorAll(".event_card"));

        let parsedEvents = events.map(event => {
            let dateText = event.querySelector("p:nth-of-type(2)")?.textContent.replace("Date: ", "").trim();
            let timeText = event.querySelector("p:nth-of-type(3)")?.textContent.replace("Time: ", "").trim();
            let attendeesText = event.querySelector("p:nth-of-type(4)")?.textContent.replace("Attendees: ", "").trim();

            let eventDate = new Date(dateText);
            let eventTime = parseTime(timeText);
            let attendees = parseInt(attendeesText) || 0;

            return {
                element: event,
                date: isNaN(eventDate) ? null : eventDate,
                time: eventTime,
                attendees: attendees
            };
        });

        // sort logic; by date & time for "Upcoming", or by attendees for "Popular"
        if (isUpcoming) {
            parsedEvents = parsedEvents
                .filter(e => e.date) // removes events with invalid dates
                .sort((a, b) => {
                    let dateComparison = a.date - b.date; // compares by date first
                    if (dateComparison !== 0) return dateComparison;
                    return a.time - b.time; // if event falls on same date, sort by time
                });
        } else {
            // sort based on the by number of attendees
            parsedEvents.sort((a, b) => b.attendees - a.attendees);
        }

        container.innerHTML = "";
        parsedEvents.forEach(eventObj => container.appendChild(eventObj.element));

        console.log("Sorted Events: ", parsedEvents);
    }

    /**
     * Parses time strings (e.g., "2:30 PM") and converts them into a numeric value.
     * - Ensures AM/PM formats are correctly converted into a 24-hour time.
     * - Used to allow proper sorting of events occurring on the same day.
     *
     * @param {string} timeString - Time string (e.g., 3:45 PM)
     * @returns {number} Total minutes since midnight
     */
    function parseTime(timeString) {
        let timeMatch = timeString.match(/(\d{1,2}):(\d{2})\s*(AM|PM|am|pm)?/);
        if (!timeMatch) return 0; // if time is invalid it defaults to 0

        let hours = parseInt(timeMatch[1], 10);
        let minutes = parseInt(timeMatch[2], 10);
        let period = timeMatch[3] ? timeMatch[3].toUpperCase() : null;

        if (period === "PM" && hours !== 12) hours += 12;
        if (period === "AM" && hours === 12) hours = 0;

        return hours * 60 + minutes; // converts hours and minutes to a single comparable value
    }
    // ensures sorting applies immediately on page load/reload
    window.addEventListener("load", updateEvents);
});