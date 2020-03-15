import string

ones = {
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

ten_position = {2:'twenty',
                3:'thirty',
                4:'fourty',
                5:'fifty',
               }

tens = {10:'ten',
        20:'twenty',
        30:'thirty',
        40:'fourty',
        50:'fifty',
       }

def main():
        
        time_input = input('Please enter the time hours first then minutes separated by space: ')
        
        print(time_input)
        
        time_split = time_input.split(' ')

        print(time_split)

        a = time_split[0]
        b = time_split[1]

        a = int(a)
        b = int(b)

        print(a)
        print(b)

        num_hour1 = (a // 10) % 10
        num_hour2 = a % 10
        num_min1 = (b // 10) % 10
        num_min2 = b % 10

        print(num_hour1)
        print(num_hour2)
        print(num_min1)
        print(num_min2)                
                
        if num_hour1 > 0:
            if num_hour1 > 1:
                hour1 = 'twenty'
                hour2 = ones[num_hour2]
                hours = (hour1,hour2)

            elif num_hour1 == 1:
                hours = teens[a]

        else:
            hours = tens[a]

        # print(f'{hours[0]} {hours[1]}')
                
        if num_min2 > 0:
            if num_min1 > 0:
                x = ten_position[num_min1]
                y = ones[num_min2]
                minutes = (x,y)
                
            if num_min1 == 0:


main()