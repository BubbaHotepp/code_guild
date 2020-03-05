import random
import string

def quantity_lower():
    x = int(input('Enter the number of lowercase letters \ndesired for your password: '))
    return x
    
def quantity_upper():
    x = int(input('Enter the number of uppercase letters \ndesired for your password: '))
    return x
    
def quantity_numbers():
    x = int(input('Enter the number of number characters \ndesired for your password: '))
    return x

def quantity_characters():
    x = int(input('Enter the number of special characters \ndesired for your password: '))
    return x

def lowercase(password):
    for i in range(0, quantity_lower()):
        password.append(random.choice(string.ascii_lowercase))
    
def uppercase(password):
    for i in range(0, quantity_upper()):
        password.append(random.choice(string.ascii_uppercase))

def numbers(password):
    for i in range(0, quantity_numbers()):
        password.append(random.choice(string.digits))
        
def characters(password):
    for i in range(0, quantity_characters()):
        password.append(random.choice(string.punctuation))


def main():
    
    password = []

    lowercase(password)
    uppercase(password)
    numbers(password)
    characters(password)

    random.shuffle(password)

    print("".join(password))

main()