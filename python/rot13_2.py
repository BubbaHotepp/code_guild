import string

def main():
    
    cypher_text = []
    user_input = input('Please enter plain text to encode: ')
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    x = int(input('Please enter the rotation amount for the cypher: '))

    for chr in user_input:

        if chr in alphabet_lower:
            cypher_text += alphabet_lower[(alphabet_lower.find(chr)+x) % 26]
        elif chr in alphabet_upper:
            cypher_text += alphabet_upper[(alphabet_upper.find(chr)+x) % 26]
        else:
            cypher_text.append(chr)
        
    print(''.join(cypher_text))

main()