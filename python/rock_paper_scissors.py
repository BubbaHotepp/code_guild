import random

def comp_choice():
    rps = ['r','p','s']
    x = random.choice(rps)
    return x

def rock_v_scissors(x):
    print(f'\nRock smashes scissors, {x}!!')

def rock_v_paper(x):
    print(f'\nPaper covers rock, {x}!!')

def scissors_v_paper(x):
    print(f'\nScissors cuts paper, {x}!!')


def main():
    print('Welcome to Rock Paper Scissors.\n')

    user_choice = input('Please enter the letter of your choice [r]ock, [p]aper, or [s]cissors: ')

    x = comp_choice()
    
    if user_choice == 'r' and x == 'p':
        winner = 'Computer wins'
        rock_v_paper(winner)
    
    elif user_choice == 'p' and x == 'r':
        winner = 'You win'
        rock_v_paper(winner)
    
    elif user_choice == 's' and x == 'p':
        winner = 'You win'
        scissors_v_paper(winner)
    
    elif user_choice == 'p' and x == 's':
        winner = 'Computer wins'
        scissors_v_paper(winner)

    elif user_choice == 's' and x == 'r':
        winner = 'Computer wins'
        rock_v_scissors(winner)

    elif user_choice == 'r' and x == 's':
        winner = 'You win'
        rock_v_scissors(winner)
    
    else:
        print('It\'s a tie, nobody wins.')
        
 
main()
        
