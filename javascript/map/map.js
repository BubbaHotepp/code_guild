let woobMap = L.map('mapid').setView([0, 0], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYnViYmFob3RlcHAiLCJhIjoiY2tiMnhvN3c3MGczOTJ2bXRyeGQ1cXRzMyJ9.n-HfORkQcVxIYPRgxp5TgA'
}).addTo(woobMap);

axios.get('https://randomuser.me/api/?results=10&format=json&dl').then(response => {
    let dataLength = response.data.results.length;
    let persons = [[],[],[],[],[],[],[],[],[],[],];
    for (let item = 0; item <= dataLength; item++) {
        console.log(response.data.results[item])
        let person = response.data.results[item]
        for (let item in response.data.results) {
            persons[item][0] = person.location.coordinates.latitude;
            persons[item][1] = person.location.coordinates.longitude;
            persons[item][2] = person.name.first + ", " + person.name.last;
            persons[item][3] = person.location.street.number + " " + person.location.street.name;
            persons[item][4] = person.location.city;   
            persons[item][5] = person.location.country;
            persons[item][6] = person.location.postcode;
        };
    };
    let markerOptions = {
        clickable: true,
        draggable: false,
    };
    for (count = 0; count < locations.length; count++) {
        marker = new L.marker([persons[count][0], persons[count][1]])
            .bindPopup(locations[count][2],
                       locations[count][3],
                       locations[count][4],
                       locations[count][5],
                       locations[count][6],
                       )
            .addTo(woobMap);
    };
});


