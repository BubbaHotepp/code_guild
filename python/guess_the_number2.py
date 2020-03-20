import random

def comp_choice():
    x = random.randint(1,10)
    return (x)

def main():

    print('The Computer has chosen a number between 1 and 10. Try to guess the number.')
    x = comp_choice()
    count = 0

    while True:

        user_choice = int(input('Please enter your guess: '))
        count += 1
        if user_choice == x:
            print(f'Your guess: {user_choice} \nYou guessed correctly, congratulations!! \nIt took you {count} tries to guess correctly.')
            break
        
        else:
            print(f'Your guess: {user_choice} \nYou have chosen poorly!')
            continue
        
main()