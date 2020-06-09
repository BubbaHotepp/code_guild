
let axios = require('axios');

axios.get('https://randomuser.me/api/?results=10&format=json&dl').then(response => {
    response.data.results.map((result)) => {
        console.log(result)
        // let dataLength = response.data.results.length;
        // for (let item = 0; item <= dataLength; item++) {
        //     let itemData = response.data.results[item]
        // }
    };
});