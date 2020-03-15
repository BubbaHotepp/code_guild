import string

def lower(x):
    return x.lower()

def space(x):
    return x.replace(' ','')

def sort_str(x):
    return sorted(x)

def main():
    first_input = input('Please input first anagram word or words to compare: ')
    second_input = input('Please input second anagram word or words to compare: ')

    first_word = lower(first_input)
    first_word = space(first_word)
    first_word = sort_str(first_word)

    second_word = lower(second_input)
    second_word = space(second_word)
    second_word = sort_str(second_word)

    if first_word == second_word:
        print(f'{first_input} and {second_input} are anagrams.')
        
    else:
        print(f'{first_input} and {second_input} are not anagrams.')
    
main()