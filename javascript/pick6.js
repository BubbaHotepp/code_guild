const numbers = [0,1,2,3,4,5];

function pick(number)
{
    return[Math.floor((Math.random() * 99) +1)];
}

let arrayLength = numbers.length;

for (let i = 0; i < arrayLength; i++) {
    console.log(numbers[i]);
    numbers[i] = pick();
}

console.log(numbers);