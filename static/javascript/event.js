window.initMap = function () {

    var locationElem = document.getElementById('event-location');
    if (!locationElem) {
        console.error("No element found with id='event-location'!");
        return;
    }
    var address = locationElem.dataset.address;


    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: { lat: 55.8730, lng: -4.2890 }
    });


    geocoder.geocode({ address: address }, function (results, status) {
        if (status === "OK") {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            alert("Geocode was not successful: " + status);
        }
    });
};


$(document).ready(function () {
    $("#attend-button").click(function () {
        var eventId = $(this).data("event-id");
        var csrfToken = $(this).data("csrf-token");

        $.post(`/glasgowgaffsapp/event/${eventId}/toggle_attendance/`, {
            'csrfmiddlewaretoken': csrfToken
        })
            .done(function (response) {
                console.log("Attendance changed:", response);
            })
            .fail(function () {
                console.log("Error processing request.");
            });
    });
});
