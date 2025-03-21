document.addEventListener("DOMContentLoaded",()=>{

    document.getElementById('contact-us-button').addEventListener("click",()=>{
    showPopupForm();
    ClearFunction();
    });
    
    document.getElementById('close-popup').addEventListener("click",()=>{
    hidePopupForm();
    ClearFunction();
    });
    
    });
    
    function showPopupForm() {
        document.getElementById("popup-form-container").style.display = "block";
        document.getElementById('contact-us-button').classList.add('no-hover');
      };
      
      function hidePopupForm() {
        document.getElementById("popup-form-container").style.display = "none";
        document.getElementById('contact-us-button').classList.remove('no-hover');
      };
    
      document.getElementById("send-email").addEventListener("click",()=>{
        alert("Email sent!")
        ClearFunction();
      });
    
      function ClearFunction() {
        document.getElementById("contact-form").reset();
      }