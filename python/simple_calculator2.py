def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def main():
    x = ''

    while x != 'done':
        first_input = input('Please enter the first number: ')
        second_input = input('Please enter the operation: ')
        third_input = input('Please enter the second number: ')

        x = int(first_input)
        y = int(third_input)

        if second_input == '*':
            z = multiply(x,y)
            print(str(first_input) + str(second_input) + str(third_input) + ' = ' + str(z))
    
        elif second_input == '/':
            z = divide(x,y)
            print(str(first_input) + str(second_input) + str(third_input) + ' = ' + str(z))

        elif second_input == '+':
            z = add(x,y)
            print(str(first_input) + str(second_input) + str(third_input) + ' = ' + str(z))

        elif second_input == '-':
            z = subtract(x,y)
            print(str(first_input) + str(second_input) + str(third_input) + ' = ' + str(z))

        x = input('Type \'done\' if you are finished or press enter to continue: ')
        
main()