import string

def main():
    
    cypher_text = []

    user_input = input('Please enter plain text to encode: ')

    alphabet = string.ascii_letters

    x = int(input('Please enter the rotation amount for the cypher: '))

    for chr in user_input:

        if chr in alphabet:
            cypher_text += alphabet[(alphabet.find(chr)+x)%52]

        elif chr not in alphabet:
            cypher_text.append(chr)
        
    print(''.join(cypher_text))

main()