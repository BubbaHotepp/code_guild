import random

def malib_choice(x):
    return random.choice(x)

def main():
    noun_input = input('Please enter 3 nouns separated by a comma: ')
    noun_list = noun_input.split(",")

    adjective_input = input('Please enter 3 adjectives separated by a comma: ')
    adjective_list = adjective_input.split(", ")

    verb_input = input('Please enter 3 verbs separated by a comma: ')
    verb_list = verb_input.split(", ")

    print(f"If you give a {madlib_choice(noun_list)} a {madlib_choice(noun_list)}, they are going to ask for a {madlib_choice(noun_list)}.  When you give them the {madlib_choice(adjective_list)} {madlib_choice(noun_list)}, they will want to {madlib_choice(verb_input)}.  When they are finished, they will {madlib_choice(verb_list)}.  Then they will {madlib_choice(verb_list)} and {madlib_choice(verb_list)} to the {madlib_choice(noun_list)}.  If not they will {madlib_choice(verb_list)} the {madlib_choice(adjective_list)} {madlib_choice(noun_list)}.")

main()
