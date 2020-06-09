let persons = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


let axios = require('axios');
axios.get('https://randomuser.me/api/?results=10&format=json&dl').then(response => {
    let dataLength = response.data.results.length;
    for (let item = 0; item <= dataLength; item++) {
        let data = response.data.results[item];
        console.log(data)
        let person = data[item];
        console.log(person)
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
});

console.log(persons[1][2])
