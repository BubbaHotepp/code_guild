
let axios = require('axios');

axios.get('https://randomuser.me/api/?results=10&format=json&dl').then(response => {
    let dataLength = response.data.results.length;
    let persons = [[],[],[],[],[],[],[],[],[],[],];
    for (let item = 0; item <= dataLength; item++) {
        let itemData = response.data.results[item]
        // console.log(itemData.location.coordinates.longitude)
        // console.log(itemData.location.coordinates)
        let itemArray = []
        let lat = itemData.location.coordinates.latitude;
        console.log(lat)
        itemArray.push(lat);
        let lon = itemData.location.coordinates.longitude;
        itemArray.push(lon);
        itemArray.push(itemData.name.first + ", " + itemData.name.last);
        itemArray.push(itemData.location.street.number + " " + itemData.location.street.name);
        itemArray.push(itemData.location.city);   
        itemArray.push(itemData.location.country);
        itemArray.push(itemData.location.postcode);
        persons.push(itemArray);
        };
//    console.log(persons[2][2])
    });