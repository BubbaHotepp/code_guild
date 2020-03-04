import random
import string

def main():
    def password(length = x):
        characters = string.punctuation + string.digits + string.ascii_letters
        return ''.join(random.choice(characters) for i in range(0, length))
    
    def user_length(x):
        x = int(input('Please enter number of characters for your password: '))
        return x

    print(f'Your random password is: {password()}')
    
main()