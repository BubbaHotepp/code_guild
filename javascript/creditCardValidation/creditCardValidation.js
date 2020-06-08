function numberToArray(numIn) {              //A function to turn a Number into an array.//
    return Array.from(Number(numIn));
};

function doubler(numberInput) {
    let numberLength = numberInput.length;             // A function that takes in a Number, converts to an array using the numberToArray
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

function reverseInt(num) {      // A function that reverses a number.
    return Number(String(num).split('').reverse().join(''))
};

let numberInput = prompt("Please enter the Credit Card number to validate: ");
console.log(numberInput);
let checkDigit = numberInput.slice(-1);
console.log(checkDigit);
let numberSliced = numberInput.slice(0,15);
console.log(numberSliced);
let numberRvrs = reverseInt(numberSliced);
console.log(numberRvrs);
let numberDoubled = doubler(numberRvrs);
console.log(numberDoubled);
let checkDigitInt = parseInt(checkDigit);
console.log(checkDigitInt);

document.write("The doubled reverse number is: ", numberDoubled);
