import random

def comp_choice():
    x = random.randint(1,10)
    return (x)

def main():

    print('The Computer has chosen a number between 1 and 10. \nYou have 10 tries to guess the correct number.')
    
    countdown = 0

    x = comp_choice()

    while countdown < 10:

        user_choice = int(input('Please enter your guess: '))
        
        if user_choice == x:
            print('You guessed correctly, congratulations!!')
            break
        
        elif user_choice != x:
            print('You have chosen poorly!')
            countdown += 1

        
main()