// reloads the button for event
const attendBtn = document.getElementById("attend-button");
if (attendBtn) {
    attendBtn.addEventListener("click", function () {
        setTimeout(() => location.reload(), 50);
    });
}