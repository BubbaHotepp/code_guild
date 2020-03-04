import random
import string

def main():
    def password(length = 10):
        characters = string.punctuation + string.digits + string.ascii_letters
        return ''.join(random.choice(characters) for i in range(length))

    print(f'Your random password is: {password()}')
    
main()