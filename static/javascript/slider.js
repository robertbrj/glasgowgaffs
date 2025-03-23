document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.getElementById("eventToggle");
    const createdEvents = document.getElementById("created_events");
    const attendingEvents = document.getElementById("attending_events");
    const createdTitle = document.getElementById("created_title");
    const attendingTitle = document.getElementById("attending_title");

    // default state: Created Events visible, Attending Events hidden
    createdEvents.style.display = "grid";
    attendingEvents.style.display = "none";
    createdTitle.classList.add("bold");
    attendingTitle.classList.remove("bold");

    // toggle switch swaps the bold effect and switches between Created Events amd Attending Events
    toggleSwitch.addEventListener("change", function () {
        console.log("Toggle switched! Checked:", this.checked);

        if (this.checked) {
            // shows attending events
            attendingEvents.style.display = "grid";
            createdEvents.style.display = "none";

            // applies bold styling
            attendingTitle.classList.add("bold");
            createdTitle.classList.remove("bold");
        } else {
            // shows created events
            createdEvents.style.display = "grid";
            attendingEvents.style.display = "none";

            // applies bold styling
            createdTitle.classList.add("bold");
            attendingTitle.classList.remove("bold");
        }
    });
});