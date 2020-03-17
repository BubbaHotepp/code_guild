import string

ones = {1:'one',
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

tens = {2:'twenty',
        3:'thirty',
        4:'fourty',
        5:'fifty',
        10:'ten',
        20:'twenty',
        30:'thirty',
        40:'fourty',
        50:'fifty',
       }

def hours(x):

    num_hour1 = (x // 10) % 10
    num_hour2 = x % 10

    if num_hour1 == 0:
        return ones[num_hour2]

    elif num_hour1 == 1:
        return teens[x] 
    
    else:
        y = tens_position[num_hour1]
        z = ones[num_hour2]
        return y + ' ' + z

def minutes(x):

    num_min1 = (x // 10) % 10
    num_min2 = x % 10
    if num_min1 == 0 and num_min2 == 0:
        return 'o\'clock'

    elif num_min1 == 0:
        return ones[num_min2]

    elif num_min1 == 1:
        return teens[num_min2]

    else:
        y = tens[num_min1]
        z = ones[num_min2]
        return y + ' ' + z

def main():

    print('Time digit to word conversion. \nPlease input the time to convert.')
    hours_input = int(input('Hours (1-12): '))
    print(hours_input)
    minutes_input = int(input('Minutes (0 - 59): '))
    print(minutes_input)
    am_pm = input('AM or PM: ')
    
    print(f'The time is: {hours(hours_input)} {minutes(minutes_input)} {am_pm}.')

main()