let numberInput = 12345;
console.log(numberInput);
function numberArray(numberIn){
    return Array.from(String(numberIn), Number);
};

function doubler(numberInput) {
    let numberLength = numberInput.length;                              // A function that takes in a Number, converts to an array using the numberToArray
    for (item = 0; item <= numberLength; item += 2) {  // then returns the resulting number.
        console.log(numberInput)
        console.log(numberInput[item]);
        numberInput[item] *= 2;
        console.log(numberInput[item]);
        console.log(numberInput);
    };
    let numberOutput = parseInt(numberInput.join(''));
    return numberOutput;
};

let arrayInt = numberArray(numberInput);
console.log(arrayInt);
let numberDoubled = doubler(arrayInt);
console.log(numberDoubled);
let stringDoubled = JSON.stringify(numberDoubled);
console.log(stringDoubled);
let arrayJoin = stringDoubled.join('');
console.log(arrayJoin);
let numberOutput = parseInt(arrayJoin);
console.log(numberOutput);