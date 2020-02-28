import random

noun_input = input('Please enter 3 nouns separated by a comma: ')

noun_list = noun_input.split(",")

adjective_input = input('Please enter 3 adjectives separated by a comma: ')

adjective_list = adjective_input.split(", ")

verb_input = input('Please enter 3 verbs separated by a comma: ')

verb_list = verb_input.split(", ")

print(f"If you give a {random.choice(noun_list)} a {random.choice(noun_list)}, they are going to ask for a {random.choice(noun_list)}.  When you give them the {random.choice(adjective_list)} {random.choice(noun_list)}, they will want to {random.choice(verb_input)}.  When they are finished, they will {random.choice(verb_list)}.  Then they will {random.choice(verb_list)} and {random.choice(verb_list)} to the {random.choice(noun_list)}.  If not they will {random.choice(verb_list)} the {random.choice(adjective_list)} {random.choice(noun_list)}.")
