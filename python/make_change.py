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
    amount = int(input('Please enter the amount of pennies to convert: '))
       
    print(f'That amount converts to: \n{quarters(amount)} quarters, \n{dimes(amount)} dimes, \n{nickels(amount)} nickels, \nand \n{pennies(amount)} pennies.')

main()