# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
def main():
    user_input = []

    while True:
        user_input = input('Please enter credit card number to verify: ')
        affirmation = input(f'{user_input} \nIs this correct? Y/N: ')
        if affirmation in ('y','Y','Yes','yes','YES','n','N','No','no','NO'):
            break
        else:
            print('Please enter only Y/N, y/n or Yes/No.')
          
    card_number = [int(i) for i in user_input]
    check_digit = card_number[-1]
    del card_number[-1]
    card_number.reverse()
        
    for i in card_number[::2]:
        x = card_number.index(i)
        card_number[x] = i * 2
    
    for i in card_number:
        if i > 9:
            x = card_number.index(i)
            card_number[x] = i - 9
    
    total = sum(card_number)
    total_check_digit = total%10
    
    if check_digit == total_check_digit:
        print('That is a valid credit card number.')
    else:
        print('That is NOT a valid credit card number.')

main()

