const readline=require('readline-sync')

function pick_six(){
    return[Math.floor(Math.random()*100)]
};

function roi(winnings,costs){
    return[(winnings - costs)/costs] 
};

function pick_loop(array_name, array_length){
    for (let i = 0; i < array_length; i++){
        array_name[i]  = pick_six()
    }

};

function number_sort(array_input) {
    array_input.sort(function(a,b){return a - b})
};

const winning_numbers = [0,0,0,0,0,0];
let wn_arrayLength = winning_numbers.length;

const pick_ticket = [0,0,0,0,0,0]; 
let pt_arrayLength = pick_ticket.length;

console.log('Welcome to Pick 6.','\n', 'How many pick tickets would you like?','\n', 'Each ticket costs $2.','\n', 'Winning picks are the following:','\n', '1 number matched wins $4.','\n', '2 numbers matched wins $7.','\n', '3 numbers matched wins $100.', '\n', '4 numbers matched wins $50,000.', '\n', '5 numbers matched wins $1,000,000.','\n', '6 numbers matched wins $25,000,000.');

// let pick_amount = readline.("How many tickets would you like to purchase?", "<enter amount>");
let pick_amount = 10

let total_ticket_cost = (pick_amount * 2);
let total_winnings = 0
let losing_tickets = 0
let winning_ticket_count = 0
let match_1 = 0
let match_2 = 0
let match_3 = 0
let match_4 = 0
let match_5 = 0
let match_6 = 0


pick_loop(winning_numbers, wn_arrayLength);

number_sort(winning_numbers);
console.log(winning_numbers);

for(let run = 0; run < pick_amount; run++){
    pick_loop(pick_ticket, pt_arrayLength)
    console.log(pick_ticket);
    let match_count = 0
    let winning_amount = 0

    for (number of pick_ticket){
        if (number  winning_numbers){
            match_count += 1
        }
    }
    switch(match_count){
        case 1:
            winning_amount = 4
            match_1 += 1
            winning_ticket_count += 1
            break;
        
        case 2:
            winning_amount = 7
            match_2 += 2
            winning_ticket_count += 1
            break;
        
        case 3:
            winning_amount = 100
            match_3 += 1
            winning_ticket_count += 1
            break;

        case 4:
            winning_amount = 50000
            match_4 += 1
            winning_ticket_count += 1
            break;
        
        case 5:
            winning_amount = 1000000
            match_5 += 1
            winning_ticket_count += 1
            break;
        
        case 6:
            winning_amount = 25000000
            match_6 += 1
            winning_ticket_count += 1
            break;
        default:
            losing_tickets += 1
        }
   total_winnings += winning_amount
};

console.log('You have won $',total_winnings,'\n','You have spent $',total_ticket_cost,'\n',
            'You have ',losing_tickets,' losing tickets.','\n','You have ',winning_ticket_count,
            ' winning tickets.','\n','Your total winnings are $',total_winnings,'\n',
            'And your return on investment is ',roi(total_winnings,total_ticket_cost),'%.')