import random

def comp_choice():
    x = random.randint(1,10)
    return (x)

def main():

    print('The Computer has chosen a number between 1 and 10. Try to guess the number.')
    
    count = 1

    x = comp_choice()

    while True:

        user_choice = int(input('Please enter your guess: '))
        
        if user_choice == x:
            print('You guessed correctly, congratulations!! \nIt took you ' + str(count) + ' tries to guess correctly.')
            break
        
        elif user_choice != x:
            print('You have chosen poorly!')
            
            if user_choice > x:
                print('Your guess is too high, guess again.')
            
            elif user_choice < x:
                print('Your guess is too low, guess again.')
            count += 1
        
main()