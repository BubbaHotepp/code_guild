def main():
    a = int(input('Please enter the amount of pennies to convert: '))
       
    def quarters(a):
        x = a // 25
        return x
    
    def dimes(x):
        x = (a - (quarters(x) * 25)) // 10
        return x
    
    def nickels(x):
        x = (a - (quarters(x) * 25) - (dimes(x) * 10)) // 5
        return x

    def pennies(x):
        x = (a - (quarters(x) * 25) - (dimes(x) * 10) - (nickels(x) * 5)) // 1
        return x

    print(f'That amount converts to: \n {quarters(a)} quarters, \n {dimes(a)} dimes, \n {nickels(a)} nickels, \n {pennies(a)} pennies')

main()