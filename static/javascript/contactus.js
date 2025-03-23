// waits until the DOM is fully loaded before assigning the event listeners
document.addEventListener("DOMContentLoaded", () => {
    const contactButton = document.getElementById('contact-us-button');
    const closeButton = document.getElementById('close-popup');
    const sendEmailButton = document.getElementById('send-email');

    // pop-up form appears, on button click "Contact Us", clears the previous form
    if (contactButton) {
        contactButton.addEventListener("click", () => {
            showPopupForm();
            ClearFunction();
        });
    }
    // close button clears the form and closes the pop-up menu
    if (closeButton) {
        closeButton.addEventListener("click", () => {
            hidePopupForm();
            ClearFunction();
        });
    }
    // displays confirmation alert on button click and clears input after user clicks "Send"
    if (sendEmailButton) {
        sendEmailButton.addEventListener("click", () => {
            alert("Email sent!");
            ClearFunction();
        });
    }
});

// displays the pop-up form and hides the hover effect on the button "Contact Us"
function showPopupForm() {
    const popup = document.getElementById("popup-form-container");
    const button = document.getElementById("contact-us-button");
    if (popup) popup.style.display = "block";
    if (button) button.classList.add('no-hover');
}

// hides the pop-up form and applies the hover effect on the button "Contact Us"
function hidePopupForm() {
    const popup = document.getElementById("popup-form-container");
    const button = document.getElementById("contact-us-button");
    if (popup) popup.style.display = "none";
    if (button) button.classList.remove('no-hover');
}

// clears the input fields in the form
function ClearFunction() {
    const form = document.getElementById("contact-form");
    if (form) form.reset();
}