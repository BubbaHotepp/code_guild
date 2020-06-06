function numberValidator() {

}

function reverseInt(num) {
    return Number(String(num).split('').reverse().join(''))
}

function doubler(intInput) {
    for (item = 0, item2 = 0; item <= intInput.length; item += item2, item2+=1 ) {
        intInput[item2] * 2
        console.log(intInput)
    }
    return intInput
}

function main() {
    let numberInput = prompt("Please enter the Credit Card number to validate: ");
    console.log(numberInput);
    let checkDigit = numberInput.slice(-1);
    console.log(checkDigit);
    let numberSliced = numberInput.slice(0,15);
    console.log(numberSliced);
    let numberInt = parseInt(numberSliced);
    let numberRvrs = reverseInt(numberInt);
    let checkDigitInt = parseInt(checkDigit);
    console.log(checkDigitInt);
    console.log(numberRvrs);
    let doubledNumber = doubler(numberRvrs)
    console.log(doubledNumber)
    document.write("The doubled reverse number is: ", doubledNumber);
}

main()