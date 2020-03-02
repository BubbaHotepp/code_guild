score_input = input('Please enter your grade score: ')

score = int(score_input)

plus_minus = score%10

def letter_grade(score):
    if 90 <= score <= 100:
        letter_grade = 'A'
    if 79 < score < 90:
        letter_grade = 'B'
    if 69 < score < 80:
        letter_grade = 'C'
    if 59 < score < 70:
        letter_grade = 'D'
    if 0 <= score < 60:
        letter_grade = 'F'
    
def qualifier(plus_minus):
    if 3 < plus_minus < 7:
        qualifier = " "
    if plus_minus >= 7:
        qualifier = "+"
    if plus_minus <= 3:
        qualifier = "-"

print(f"Your grade is: {letter_grade} {qualifier}")
