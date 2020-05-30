function pickSix(arrayName){
    for (let i = 0; i < arrayName.length; i++){
        arrayName[i] = Math.floor(Math.random()*100)
    };
};

function ticketCompare(arrayName1, arrayName2, tickets){

    let totalWinnings = 0;

    for(let run = 0; run < tickets; run++){
        pickSix(arrayName2);
        console.log(arrayName1);
        console.log(arrayName2)
        console.log('\n')
        let matchCount = 0;
        let winningAmount = 0;
    
        for (let i=0; i < arrayName1.length; i++){
            if (arrayName1[i] === arrayName2[i]){
                matchCount +=1
                console.log(matchCount)
            };
        };
    
        switch(matchCount){
            case 1:
                winningAmount = 4;
                break;
            
            case 2:
                winningAmount = 7;
                break;
            
            case 3:
                winningAmount = 100;
                break;
    
            case 4:
                winningAmount = 50000;
                break;
            
            case 5:
                winningAmount = 1000000;
                break;
            
            case 6:
                winningAmount = 25000000;
                break;

            default:
                winningAmount = 0;
                break;
            }
       totalWinnings += winningAmount;
    };
    return(totalWinnings)
};

function roi(winnings,costs){
    return[(winnings - costs)/costs];
};

function main(){

    console.log('Welcome to Pick 6.','\n', 'Winning picks are the following:','\n', '1 number matched wins $4.','\n', '2 numbers matched wins $7.','\n', '3 numbers matched wins $100.', '\n', '4 numbers matched wins $50,000.', '\n', '5 numbers matched wins $1,000,000.','\n', '6 numbers matched wins $25,000,000.');

    let ticketAmount = 100;
    let totalTicketCost = (ticketAmount * 2);
    let winningNumbers = [0,0,0,0,0,0];
    let userTicket = [0,0,0,0,0,0];

    let wnArrayLength = 6;
    pickSix(winningNumbers);

    balance = ticketCompare(winningNumbers, userTicket, ticketAmount,) 

    console.log('You have won $', balance,'\n','You have spent $',totalTicketCost,'\n',
                'And your return on investment is ', roi(balance,totalTicketCost),'%.');
};

main()