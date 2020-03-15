import string

ones = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
       }

teens = {11:'eleven',
         12:'twelve',
         13:'thirteen',
         14:'fourteen',
         15:'fifteen',
         16:'sixteen',
         17:'seventeen',
         18:'eighteen',
         19:'nineteen',
        }

tens = {2:'twenty',
        3:'thirty',
        4:'fourty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety',
       }

def main():
        
        num_input = int(input('Please enter a number up to 3 digits long: '))

        a = num_input % 10
        b = (num_input // 10) % 10
        
        first = ones[a]
                
        if b > 1:
                second = tens[b]
                print(f'{num_input} is {second} {first}.')
                
        elif b == 1:
                x = (str(b),str(a))
                y = int(''.join(x))
                z = teens[y]
                print(f'{num_input} is {z}.')
                
main()