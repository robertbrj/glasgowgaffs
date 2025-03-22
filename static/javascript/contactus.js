// Only run once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const contactButton = document.getElementById('contact-us-button');
    const closeButton = document.getElementById('close-popup');
    const sendEmailButton = document.getElementById('send-email');

    if (contactButton) {
        contactButton.addEventListener("click", () => {
            showPopupForm();
            ClearFunction();
        });
    }

    if (closeButton) {
        closeButton.addEventListener("click", () => {
            hidePopupForm();
            ClearFunction();
        });
    }

    if (sendEmailButton) {
        sendEmailButton.addEventListener("click", () => {
            alert("Email sent!");
            ClearFunction();
        });
    }
});

function showPopupForm() {
    const popup = document.getElementById("popup-form-container");
    const button = document.getElementById("contact-us-button");
    if (popup) popup.style.display = "block";
    if (button) button.classList.add('no-hover');
}

function hidePopupForm() {
    const popup = document.getElementById("popup-form-container");
    const button = document.getElementById("contact-us-button");
    if (popup) popup.style.display = "none";
    if (button) button.classList.remove('no-hover');
}

function ClearFunction() {
    const form = document.getElementById("contact-form");
    if (form) form.reset();
}