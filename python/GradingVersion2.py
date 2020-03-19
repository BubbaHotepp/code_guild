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
    if (x % 10) > 6:
        return '+'
    if (x % 10) < 4:
        return '-'

def main():
    score_input = int(input('Please enter your number score: '))

    print(f'Your letter grade is: {grade_conversion(score_input)}{grade_qualifier(score_input)}.')

main()