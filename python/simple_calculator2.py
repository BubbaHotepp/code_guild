def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def main():
    
    while True:
        first_input = input('Please enter the first number: ')
        second_input = input('Please enter the operation, \n+ for addition \n- for subtraction \n* for multiplication or \n/ for division: ')
        third_input = input('Please enter the second number: ')
        x = float(first_input)
        y = float(third_input)

        if second_input == '*':
            z = multiply(x,y)
            print(f'{first_input} {second_input} {third_input} = {z}')
    
        elif second_input == '/':
            z = divide(x,y)
            print(f'{first_input} {second_input} {third_input} = {z}')

        elif second_input == '+':
            z = add(x,y)
            print(f'{first_input} {second_input} {third_input} = {z}')

        elif second_input == '-':
            z = subtract(x,y)
            print(f'{first_input} {second_input} {third_input} = {z}')

        repeat = input('Type \'done\' if you are finished or press enter to continue: ')
        
        if repeat == 'done':
            break
        else:
            continue
        
main()