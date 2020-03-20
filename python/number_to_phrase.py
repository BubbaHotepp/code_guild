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
        
        while True:
                try:
                        num_input = int(input('Please enter a number up to 2 digits long: '))

                        a = num_input % 10
                        b = (num_input // 10) % 10
                               
                        if b > 1:
                                second = tens[b]
                                if a > 0:
                                        first = ones[a]                
                                        print(f'{num_input} is {second} {first}.')
                                
                                else:
                                        print(f'{num_input} is {second}.')

                        elif b == 1:
                                if a > 0:
                                        x = (str(b),str(a))
                                        y = int(''.join(x))
                                        z = teens[y]
                                        print(f'{num_input} is {z}.')
                                else:
                                        print(f'{num_input} is ten.')                        
                        else:
                                first = ones[a]
                                print(f'{num_input} is {first}.')
                                
                        break
                
                except ValueError:
                        print('Please enter numbers only.')
                
main()