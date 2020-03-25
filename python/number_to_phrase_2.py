import string

ones = {0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
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

tens = {10:'ten',
        2:'twenty',
        3:'thirty',
        4:'fourty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety',
       }

hundreds = {1:'one hundred',
            2:'two hundred',
            3:'three hundred',
            4:'four hundred',
            5:'five hundred',
            6:'six hundred',
            7:'seven hundred',
            8:'eight hundred',
            9:'nine hundred',
           } 

def main():
        
        while True:
                try:
                        num_input = int(input('Please enter a number up to 3 digits long: '))

                        a = num_input % 10
                        b = (num_input // 10) % 10
                        c = (num_input // 100)
                                                        
                        if c == 0:
                    
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
                                        print(f'{num_input} is {first}')

                                
                        else:
                                third = hundreds[c]
                                if b > 1 :
                                        second = tens[b]
                                        if a > 0:
                                                first = ones[a]
                                                print(f'{num_input} is {third} {second} {first}.')

                                elif b == 1:
                                        if a > 0:
                                                x = (str(b),str(a))
                                                y = int(''.join(x))
                                                z = teens[y]
                                                print(f'{num_input} is {third} {z}.')
                                        else:
                                                print(f'{num_input} is {third} ten.')

                                else:
                                        if a == 0:
                                                print(f'{num_input} is {third}.')
                                        else:
                                                x = ones[a]
                                                print(f'{num_input} is {third} and {x}')
                        break

                except ValueError:
                        print('Please enter numbers only.')
main()