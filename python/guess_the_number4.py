import random

def comp_choice():
    x = random.randint(1,10)
    return (x)

def main():

    print('The Computer has chosen a number between 1 and 10. Try to guess the number.')
    
    x = comp_choice()

    last_guess = 0

    while True:

        user_choice = int(input('Please enter your guess: '))
        
        if user_choice == x:
            print('You guessed correctly, congratulations!! \nIt took you ' + str(count) + ' tries to guess correctly.')
            break
        
        elif user_choice != x:
            print('You have chosen poorly!')
            
            if last_guess == 0:
                print('Try again.')
            
            elif abs(user_choice - x) > abs(last_guess - x):
                print('You\'re getting colder.')
            
            elif abs(user_choice - x) < (last_guess - x):
                print('You\'re getting warmer!!')
            
            last_guess = user_choice

            count += 1
        
main()