import random

def main():

    x = int(input('Please choose a number between 1 and 10: '))
    
    count = 1

    while True:

        y = random.randint(1,10)
    
        print('Computer guesses: ' + str(y) )
              
        if y == x:
            print('Yay, the computer got it! \nThe computer guessed correctly in ' + str(count) + ' tries.')
            break
        
        elif y != x:
            print('The computer has chosen poorly.')
            count += 1
        
main()