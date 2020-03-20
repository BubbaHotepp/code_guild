import string

ones = {1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        6:'VI',
        7:'VII',
        8:'VIII',
        9:'IX',
        10:'X',
       }

tens = {1:'X',
        2:'XX',
        3:'XXX',
        4:'XL',
        5:'L',
        6:'LX',
        7:'LXX',
        8:'LXXX',
        9:'XC',
       }

hundreds = {1:'C',
            2:'CC',
            3:'CCC',
            4:'CD',
            5:'D',
            6:'DC',
            7:'DCC',
            8:'DCC',
            9:'CM',
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
                                        if a > 0:
                                                second = tens[b]
                                                first = ones[a]
                                                print(f'{num_input} is {second}{first}.')
                                        else:
                                                second = tens[b]
                                                print(f'{num_input} is {second}.')
                                else:
                                        if a > 0:
                                                first = ones[a]
                                                print(f'{num_input} is {first}.')
                                        else:
                                                print('There is no zero in the roman system.')
                        else:
                                if b > 0:
                                        if a > 0:
                                                third = hundreds[c]
                                                second = tens[b]
                                                first = ones[a]
                                                print(f'{num_input} is {third}{second}{first}.')
                                        else:
                                                third = hundreds[c]
                                                second = tens[b]
                                                print(f'{num_input} is {third}{second}')

                        break
                
                except ValueError:
                        print('Please enter numbers only.')               
                
main()