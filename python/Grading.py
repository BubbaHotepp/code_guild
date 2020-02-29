grade_input = input("Please enter grade score: ")

x = int(grade_input)

if 89 < x <= 100:
    print("Your grade is an A")

if 79 < x < 90:
    print("Your grade is a B")

if 69 < x < 80:
    print("Your grade is a C")

if 59 < x < 70:
    print("Your grade is a D")

if 0 <= x < 60:
    print("Your grade is an F")

    