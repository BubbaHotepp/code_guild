def score():
    x = int(input('Please enter your grade score: '))
    return x

def letter_grade(x):
       
    if 89 < x <= 100:
        x = 'A'
    elif 79 < x < 90:
        x = 'B'
    elif 69 < x < 80:
        x = 'C'
    elif 59 < x < 70:
        x = 'D'
    else:
        x = 'F'
    return x

def qualifier(x):
    if 3 < x < 7:
        x = ' '
    elif x >= 7:
        x = '+'
    else:
        x = '-'
    return x

z = score()

print(f'Your grade is: {letter_grade(z)}{qualifier(z)}')
