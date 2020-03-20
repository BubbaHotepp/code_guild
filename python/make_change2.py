def quarters(x):
    y = x // 25
    return y

def dimes(x):
    y = (x - (quarters(x) * 25)) // 10
    return y

def nickels(x):
    y = (x - (quarters(x) * 25) - (dimes(x) * 10)) // 5
    return y

def pennies(x):
    y = (x - (quarters(x) * 25) - (dimes(x) * 10) - (nickels(x) * 5)) // 1
    return y

def main():
    
    input_amount = float(input('Please enter the dollar amount to convert: '))
    amount = input_amount * 100
       

    print(f'That amount converts to: \n{quarters(amount)} quarters, \n{dimes(amount)} dimes, \n{nickels(amount)} nickels,\nand \n{pennies(amount)} pennies')

main()