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

def main():
    grade_input = int(input("Please enter grade score: "))

    print(f'Your letter grade is: {grade_conversion(grade_input)}')  

main()   