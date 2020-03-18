# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
def main():
    user_input = []

    while True:
        try:
            user_input = input('Please enter credit card number to verify: ')
            
        except ValueError:
                print('Please enter numbers only.')

        try:
            affirmation = input(f'{user_input} \nIs this correct? Y/N: ')
            if affirmation not in ('y','Y','Yes','yes','YES','n','N','No','no','NO'):
                raise ValueError
        except ValueError:
                print('Please enter only Y/N, y/n or Yes/No.')
        else:
            break
   
    card_number = [int(i) for i in user_input]
    
    check_digit = card_number[-1]

    del card_number[-1]
    
    card_number.reverse()
    
    doubled = [i*2 for i in card_number[::2]]
    non_doubled = [i * 1 for i in card_number[1::2]]
        
    mixed = [None]*(len(doubled)+len(non_doubled))
    mixed[::2] = doubled
    mixed[1::2] = non_doubled
    
    for i in mixed:
        if i > 9:
            a = mixed.index(i)
            mixed[a] = i - 9
    
    total = sum(mixed)
    total_check_digit = total%10
    if check_digit == total_check_digit:
        print('That is a valid credit card number.')
    else:
        print('That is NOT a valid credit card number.')
main()

