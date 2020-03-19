def grade_conversion(x):
    if 89 < x <= 100:
        return 'A'
    elif 79 < x < 90:
        return 'B'
    elif 69 < x < 80:
        return 'C'
    elif 59 < x < 70:
        return 'D'
    else:
        return 'F'
    
def grade_qualifier(x):
    if (x % 10) >= 7:
        return '+'
    elif 7 > (x % 10) > 3:
        return ''
    else:
        return '-'
        
def main():
    while True:
        score_input = int(input('Please enter your grade score: '))
        print(f'Your letter grade is: {grade_conversion(score_input)}{grade_qualifier(score_input)}')
        repeat_input = input('Would you like to convert another grade score? (y/n): ')
        if repeat_input in ('y','Y'):
            continue
        else:
            break

main()