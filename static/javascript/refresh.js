/* reloads the page shortly after clicking the "Attend" button
 allows AJAX changes to be reflected in the user interface. */
const attendBtn = document.getElementById("attend-button");
if (attendBtn) {
    attendBtn.addEventListener("click", function () {
        setTimeout(() => location.reload(), 50);
    });
}