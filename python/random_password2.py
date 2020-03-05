import random
import string

def main():
    
    def passwrd_length():
        length = input('Please enter the number of characters \nto be used in your password: ')
        x = int(length)
        return x
    
    x = passwrd_length()
    
    def password(x):
        characters = string.punctuation + string.digits + string.ascii_letters
        return ''.join(random.choice(characters) for i in range(0, x))
    
    counter = 0

    while counter < 6:
        counter = counter + 1
        print(f'Your random password is: {password(x)}')

main()