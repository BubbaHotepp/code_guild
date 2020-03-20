import random
import string

def pick_six():

    numbers = []
    counter = 0

    while counter < 6:

        x = random.randint(1,99)
        numbers.append(x)
        counter += 1
    
    return numbers

def main():

    print('Welcome to the Pick 6 Lotto.')
    
    ticket_cost = 0
    total_winnings = 0
    match_1 = 0
    match_2 = 0
    match_3 = 0
    match_4 = 0
    match_5 = 0
    match_6 = 0
    winning_ticket = pick_six()
    winning_ticket.sort()
    
    game_runs = input('How many picks would you like to try?: ')

    x = 0
    
    while x < int(game_runs):

        user_ticket = pick_six()
        user_ticket.sort()
        
        ticket_cost += 2
        
        match_count = 0
        
        winning_amount = 0

        for ele in user_ticket:

            if ele in winning_ticket:
                match_count += 1
        
        if match_count == 1:
            winning_amount = 4
            match_1 += 1
        
        if match_count == 2:
            winning_amount = 7
            match_2 += 1
        
        if match_count == 3:
            winning_amount = 100
            match_3 += 1
        
        if match_count == 4:
            winning_amount = 50000
            match_4 += 1
        
        if match_count == 5:
            winning_amount = 1000000
            match_5 += 1
        
        elif match_count == 6:
            winning_amount = 25000000
            match_6 += 1

        x += 1
        total_winnings += winning_amount            
        
        print(user_ticket)
        print(winning_ticket)
        print(match_count)

    print(f'\nYou\'re winning total amount is: {total_winnings}')
    print(f'Your\'re total ticket cost is: {ticket_cost}')
    print(f'You have matched 1 number {match_1} times.')
    print(f'You have matched 2 number {match_2} times.')
    print(f'You have matched 3 number {match_3} times.')
    print(f'You have matched 4 number {match_4} times.')
    print(f'You have matched 5 number {match_5} times.')
    print(f'You have matched 6 number {match_6} times.')
    
main()