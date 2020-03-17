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
    user_input1 = input('Please enter your first card \n(1-10,J,Q,K,A): ')
    user_input2 = input('Please enter your second card \n(1-10,J,Q,K,A): ')
    user_input1 = str.lower(user_input1)
    user_input2 = str.lower(user_input2)
    user_card1 = int(card_value[user_input1])
    user_card2 = int(card_value[user_input2])

    if (user_card1 + user_card2) != 11:
        card_total = user_card1 + user_card2
        while card_total < 21:
            while card_total < 17:
                print(f'{card_total} You should hit.')
                x = input('Enter your next card: ')
                y = int(card_value[x])
                card_total += y
            
                if card_total > 21:
                    print(f'{card_total} You\'ve busted.')
                    break
                elif card_total == 21:
                    print(f'{card_total}, you can\'t hit anymore.')
                    break
                else:
                    print(f'{card_total} you should hold.')
                    break
            if card_total >= 17:
                break                
        
    elif (user_card1 + user_card2) == 11:
        print('Blackjack, you win.')

main()

            
        