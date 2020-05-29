function pick_six(array_name, array_length){
    for (let i = 0; i < array_length; i++){
        array_name[i] = Math.floor(Math.random()*100)
    };
};

function ticket_compare(pick_amount){
    pt_arrayLength = 6;

    for(let run = 0; run < pick_amount; run++){
        pick_loop(pick_ticket, pt_arrayLength);
        console.log(pick_ticket);
        let match_count = 0;
        let winning_amount = 0;
    
        for (let i=0; i < pt_arrayLength; i++){
            if (pick_ticket[i] === winning_numbers[i]){
                match_count +=1
            };
        };
    
        switch(match_count){
            case 1:
                winning_amount = 4;
                match_1 += 1;
                winning_ticket_count += 1;
                break;
            
            case 2:
                winning_amount = 7;
                match_2 += 2;
                winning_ticket_count += 1;
                break;
            
            case 3:
                winning_amount = 100;
                match_3 += 1;
                winning_ticket_count += 1;
                break;
    
            case 4:
                winning_amount = 50000;
                match_4 += 1;
                winning_ticket_count += 1;
                break;
            
            case 5:
                winning_amount = 1000000;
                match_5 += 1;
                winning_ticket_count += 1;
                break;
            
            case 6:
                winning_amount = 25000000;
                match_6 += 1;
                winning_ticket_count += 1;
                break;
            default:
                losing_tickets += 1;
            }
       total_winnings += winning_amount;
    };
};

function roi(winnings,costs){
    return[(winnings - costs)/costs];
};

function main(){

console.log('Welcome to Pick 6.','\n', 'Winning picks are the following:','\n', '1 number matched wins $4.','\n', '2 numbers matched wins $7.','\n', '3 numbers matched wins $100.', '\n', '4 numbers matched wins $50,000.', '\n', '5 numbers matched wins $1,000,000.','\n', '6 numbers matched wins $25,000,000.');

let pick_amount = 1000;
let total_ticket_cost = (pick_amount * 2);
let total_winnings = 0;
let losing_tickets = 0;
let winning_ticket_count = 0;

pick_(winning_numbers, wn_arrayLength);
console.log(winning_numbers);

console.log('You have won $',total_winnings,'\n','You have spent $',total_ticket_cost,'\n',
            'You have ',losing_tickets,' losing tickets.','\n','You have ',winning_ticket_count,
            ' winning tickets.','\n','Your total winnings are $',total_winnings,'\n',
            'And your return on investment is ',roi(total_winnings,total_ticket_cost),'%.');

};