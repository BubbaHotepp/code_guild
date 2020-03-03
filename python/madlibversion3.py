import random



while True:
    user_input = input('Would you like to play?: ')

    if user_input == 'y':
        noun_input = input('Please enter 3 sciency sounding nouns separated by commas: ')
        noun_list = noun_input.split(',')

        verb_input = input('Please enter 3 pretentious verbs separated by commas: ')
        verb_list = verb_input.split(',')

        adjective_input = input('Please enter 3 snarky adjectives separated by commas: ')
        adjective_list = adjective_input.split(',')

        while True:
            user_input2 = input('Would you like to read the story? \n Enter y/n to continue: ')

            if user_input2 == 'y':
                print(f'There once was a Doctor of {random.choice(noun_list)}. \nWho spent his days dreaming of {random.choice(noun_list)}. \nBut when he {random.choice(verb_list)} it all fell apart, \nUntil his {random.choice(adjective_list)} {random.choice(noun_list)} {random.choice(verb_list)} \nand he couldn\'t think anymore.')
                continue
            elif user_input2 == 'n':
                print('I don\'t blame you, I wouldn\'t want to hear that nonsense either.')
                break
            else:
                print('Please enter only y/n to continue:')
    
    elif user_input == 'n':
        print('Maybe next time.')
        break

    else:
        print('Please only enter y/n to continue:')

