import random

def comp_choice():
    rps = ['r','p','s']
    x = random.choice(rps)
    return x

def rock_v_scissors(x):
    return f'\nRock smashes scissors, {x}!!'

def rock_v_paper(x):
    return f'\nPaper covers rock, {x}!!'

def scissors_v_paper(x):
    return f'\nScissors cuts paper, {x}!!'

def game(x,y):
    if x == 'r' and y == 'p':
        winner = 'Computer wins'
        return rock_v_paper(winner)
   
    elif x == 'p' and y == 'r':
        winner = 'You win'
        return rock_v_paper(winner)
    
    elif x == 's' and y == 'p':
        winner = 'You win'
        return scissors_v_paper(winner)
    
    elif x == 'p' and y == 's':
        winner = 'Computer wins'
        return scissors_v_paper(winner)

    elif x == 's' and y == 'r':
        winner = 'Computer wins'
        return rock_v_scissors(winner)

    elif x == 'r' and y == 's':
        winner = 'You win'
        return rock_v_scissors(winner)
    
    else:
        return 'It\'s a tie, nobody wins.'

def main():
    print('Welcome to Rock Paper Scissors. \nMake your choice and try to beat the computer.')
    
    while True:
        user_choice = input('Please enter the letter of your choice [r]ock, [p]aper, or [s]cissors: ')
        if user_choice not in ('R','r','P','p','S','s'):
            print('Please ONLY enter \'R\'/\'r\', \'P\'/\'p\', or \'S\'/\'s\': ')
        else:
            break
     
    computer = comp_choice()
    print(f'{game(user_choice,computer)}') 
 
main()
        
