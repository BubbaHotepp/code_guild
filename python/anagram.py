def reverse_string(x):
    return x[::-1]

def compare(x,y):
    if x == y:
        return True

    else:
        return False

def main():

    user_input = input('Please enter a word you think is an anagram: ')
    print(user_input)
    input_reversed = reverse_string(user_input)
    print(input_reversed)
    x = compare(user_input, input_reversed)
    print(x)

    if x is True:

        print(f'{user_input} is a palindrome.')

    else:
        print(f'{user_input} is not a palindrome.')

main()