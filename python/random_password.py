import random
import string

def character_choice(x):
    characters = string.punctuation + string.digits + string.ascii_letters
    return x.append(random.choice(characters))

def main():
    password_characters = []
    counter = 0
    while counter < 10:
        character_choice(password_characters)
        counter += 1
    password = ''.join(password_characters)
    print(f'Your random password is: {password}')
    
main()