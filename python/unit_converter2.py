def meters(x):
    
    if x == 'f':
        x = 0.3408
        return x
        
    elif x == 'k':
        x = 1000
        return x
        
    elif x == 'm':
        x = 1609.34
        return x

def main():
    
    unit = input('What is the unit you wish to convert to meters \n[m]iles, [k]ilometers, or [f]eet? \nPlease enter the appropriate letter: ')
    distance = input('Please enter the distance: ')
    conversion = float(meters(unit))
    x = float(distance) * conversion
    
    print(f'{distance} {unit} equals {x} meters.' )

main()