let woobMap = L.map('mapid').setView([0, 0], 1);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYnViYmFob3RlcHAiLCJhIjoiY2tiMnhvN3c3MGczOTJ2bXRyeGQ1cXRzMyJ9.n-HfORkQcVxIYPRgxp5TgA'
}).addTo(woobMap);

// let marker = marker.bindPopup().openPopup();

let popup = L.popup()
    .setLatLng([0,0])
    .setContent("Test")
    .openOn(woobMap);

const axios = require('axios');

async function makeGetRequest() {
    let randomUser = await axios.get('https://randomuser.me/api/');
    let data = randomUser.data;
    console.log(data)
}