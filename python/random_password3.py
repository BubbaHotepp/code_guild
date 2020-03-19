import random
import string

def random_generator(x,y,z):
    counter = 0
    while counter < x:
        y.append(random.choice(z))
        counter +=1    
            
def lowercase(x):
    lower = int(input('Enter the number of lowercase letters \ndesired for your password: '))
    random_generator(lower,x,string.ascii_lowercase)
    return x
    
def uppercase(x):
    upper = int(input('Enter the number of uppercase letters \ndesired for your password: '))
    random_generator(upper,x,string.ascii_uppercase)
    return x

def numbers(x):
    number = int(input('Enter the number of number characters \ndesired for your password: '))
    random_generator(number,x,string.digits)
    return x
        
def characters(x):
    character = int(input('Enter the number of special characters \ndesired for your password: '))
    random_generator(character,x,string.punctuation)
    return x

def main():
    password = []

    lowercase(password)
    uppercase(password)
    numbers(password)
    characters(password)
    random.shuffle(password)

    print("".join(password))

main()