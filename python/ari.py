import string

def sentence_count(x):     
    x = ''.join(chr for chr in x)
    x = x.replace(' ', '')
    x = x.replace('?','.')
    x = x.replace('!','.')
    x = x.replace(':','.')
    x = x.replace(';','.')
    sentence_file = x.split('.')
    return len(sentence_file)
        
def word_count(x):
    exclude = set(string.punctuation)
    word_list = ''.join(chr for chr in x if chr not in exclude)
    word_list = word_list.split()
    return len(word_list)    
    
def character_count(x):
    exclude = set(string.punctuation)
    character_list = ''.join(chr for chr in x if chr not in exclude)
    character_list = character_list.replace(' ','')
    character_list = character_list.replace('\'','')
    character_list = list(character_list)
    return len(character_list)
    
ari_scale = {1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
             2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
             3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
             4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
             5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
             6: {'ages': '10-11', 'grade_level':    '5th Grade'},
             7: {'ages': '11-12', 'grade_level':    '6th Grade'},
             8: {'ages': '12-13', 'grade_level':    '7th Grade'},
             9: {'ages': '13-14', 'grade_level':    '8th Grade'},
            10: {'ages': '14-15', 'grade_level':    '9th Grade'},
            11: {'ages': '15-16', 'grade_level':   '10th Grade'},
            12: {'ages': '16-17', 'grade_level':   '11th Grade'},
            13: {'ages': '17-18', 'grade_level':   '12th Grade'},
            14: {'ages': '18-22', 'grade_level':      'College'}
            }



def main():
    text_input = input('Please enter the text name to be evaluated: ')
    
    sentence_file = open(text_input, encoding='utf8')
    word_file = open(text_input, encoding='utf8')
    character_file = open(text_input, encoding='utf8')
    
    x = sentence_count(sentence_file)
    y = word_count(word_file)
    z = character_count(character_file)
    ari_temp = (4.71 * (z/y)) + (0.5 * (y/x)) - 21.43
    ari_remainder = ari_temp%1
    
    if ari_remainder > 0:
        ari_remainder = 1
    else:
        ari_remainder = 0
    
    ari = int(ari_temp + ari_remainder)
    
    print(f'The Automated Readability Index (ARI) for: {text_input}  \n is {ari_scale[ari]}.')  
        
main()