import string

def split(x):
    return [char for char in x]

def int_conv(x):
    for i in range(0, len(x)):
        x[i] = int(x[i])

def encode(x):
    x 

def main():
    user_input = input('Please enter plain text to encode: ')

    input_split = (split(user_input))

    print(input_split)

    ascii_conv = []
    for ele in input_split: 
        ascii_conv.extend(ord(num) for num in ele)

    print(ascii_conv)
    
    x = 13

    encode = [i for i in ascii_conv]

    print(encode)

    char_conv = [chr(ascii) for ascii in encode]

    print(char_conv)
    
    

    

main()