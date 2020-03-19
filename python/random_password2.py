import random
import string

def password_length():
    length = int(input('Please enter the number of characters \nto be used in your password: '))
    return length

def character_choice(x):
    characters = string.punctuation + string.digits + string.ascii_letters
    return x.append(random.choice(characters))

def main():
    password_characters = []
    x = password_length()  
    counter = 0

    while counter <= x:
        character_choice(password_characters)
        counter += 1

    password = ''.join(password_characters)
    print(f'Your random password is: {password}')

main()