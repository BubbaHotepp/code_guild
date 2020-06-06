let numberInput = 12345;
console.log(numberInput);
function numberArray(numberStr){
    return Array.from(String(numberStr), Number);
}
let arrayInt = numberArray(numberInput);
console.log(arrayInt);
let arrayJoin = arrayInt.join('');
console.log(arrayJoin);
let numberStr = JSON.stringify(arrayJoin);
console.log(numberStr);
let numberInt = Number(numberStr)
console.log(numberInt);