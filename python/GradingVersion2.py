score = input("Please enter your number score: ")

grade_output = "Your letter grade is: "

x = int(score)

y = "1"

if x %10>6:
    z = "+"

if x %10<4:
    z = "-"

if 89 < x <= 100:
    y = "A"

if 79 < x < 90:
    y = "B"

if 69 < x < 80:
    y = "C"

if 59 < x < 70:
    y = "D"

if 0 <= x < 60:
    y = "F"

b = y + z

print(grade_output + b)


