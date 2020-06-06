function doubler(numberInput) {
    

    for (item = 0; item <= numberArray.length; item += 2) {
        console.log(numberArray[item])
        numberArray[item] * 2
        console.log(numberArray[item])
        console.log(numberArray)
    }
    let numberOutput = numberArray.join('')
    return numberOutput
}
function reverseInt(num) {
    return Number(String(num).split('').reverse().join(''))
}


let numberInput = prompt("Please enter the Credit Card number to validate: ");
console.log(numberInput);
let checkDigit = numberInput.slice(-1);
console.log(checkDigit);
let numberSliced = numberInput.slice(0,15);
console.log(numberSliced);
let numberDoubled = doubler(numberSliced);
console.log(numberDoubled);
let numberRvrs = reverseInt(numberDoubled);
console.log(numberRvrs);
let checkDigitInt = parseInt(checkDigit);
console.log(checkDigitInt);

document.write("The doubled reverse number is: ", numberRvrs);
