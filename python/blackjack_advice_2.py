card_value = {'2':2,
              '3':3,
              '4':4,
              '5':5,
              '6':6,
              '7':7,
              '8':8,
              '9':9,
              '10':10,
              'j':10,
              'q':10,
              'k':10,
              'a':1,
             }

def main():
    user_input1 = ''
    user_input2 = ''
    
    while user_input1 not in card_value:
        user_input1 = input('Please enter your first card \n(2-10,J,Q,K,A): ')
        if not user_input1 in card_value:
            print('Please enter only 2-10,J,Q,K or A.')
    
    while user_input2 not in card_value:
        user_input2 = input('Please enter your second card \n(2-10,J,Q,K,A): ')
        if not user_input2 in card_value:
            print('Please enter only 2-10,J,Q,K or A.')

    user_input1 = str.lower(user_input1)
    user_input2 = str.lower(user_input2)
    user_card1 = int(card_value[user_input1])
    user_card2 = int(card_value[user_input2])

    card_total = 0

    if user_card1 == 1 or user_card2 == 1:
        
        if card_total == 11:
            print('Blackjack, you win.')

        elif user_card1 == 1 and user_card2 == 1:
            card_total = 12
                    
        elif user_card1 == 1:
            card_total = user_card2 + 11

        else:
            card_total = user_card1 + 11
            
    else:
        
        card_total = user_card1 + user_card2
                  
    while card_total <= 21:

        if card_total > 21:
            print(f'{card_total} You\'ve busted.')
            break
                
        elif card_total == 21:
            print(f'{card_total}, you can\'t hit anymore.')
            break
                
        elif card_total >= 17:
            print(f'{card_total} you should hold.')
            break
        
        else:
            print(f'{card_total} You should hit.')
            next_card = input('Enter your next card: ')
            x = str.lower(next_card)
            y = int(card_value[x])
            if y > 1:
                card_total += y
            else:
                if card_total <= 10:
                    card_total += 11
                else:
                    card_total += 1 
           
main()

            
        