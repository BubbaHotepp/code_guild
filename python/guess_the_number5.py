import random

def main():

    x = int(input('Please choose a number between 1 and 10: '))
    
    count = 0

    while True:

        y = random.randint(1,10)
        count += 1
        print(f'Computer guesses: {y}')
              
        if y == x:
            print(f'Yay, the computer got it! \nThe computer guessed correctly in {count} tries.')
            break
        
        else:
            print('The computer has chosen poorly.')
            
main()