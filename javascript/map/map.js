let woobMap = L.map('mapid').setView([0, 0], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYnViYmFob3RlcHAiLCJhIjoiY2tiMnhvN3c3MGczOTJ2bXRyeGQ1cXRzMyJ9.n-HfORkQcVxIYPRgxp5TgA'
}).addTo(woobMap);

// let marker = marker.bindPopup().openPopup();

// let popup = L.popup()
//     .setLatLng([0,0])
//     .setContent("Test")
//     .openOn(woobMap);

let markerOptions = {
    clickable: true,
    draggable: false,
};

let axios = require('axios');

axios.get('https://randomuser.me/api/?results=10&format=json&dl').then(response => {
    let dataLength = response.data.results.length;
    for (let item = 0; item <= dataLength; item++) {
        for (let item in response.data.results) {
            let person = response.data.results[item];
            let lat = person.location.coordinates.latitude;
            let long = person.location.coordinates.longitude;

            let popup = L.popup()
                .setLatLng([lat,long])
                .setContent("<p>Name: </p>", person.name.first, person.name.last,
                            "<br><p>Address:</p>", person.location.street.number, person.location.street.name,
                            "<br><p>City: </p>", person.location.city,
                            "<br><p>Country: </p>", person.location.country,
                            "<br><p>Postcode: </p>", person.location.postcode,
                            )
                .openOn(woobMap);

            let marker = L.marker([lat, long], markerOptions);
            marker.bindPopup(popup);
        }
    }
});

