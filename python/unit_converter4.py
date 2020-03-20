def meters(x):
    
    if x == 'ft':
        x = 0.3408
        return x
        
    elif x == 'km':
        x = 1000
        return x
        
    elif x == 'mi':
        x = 1609.34
        return x
    
    elif x == 'yd':
        x = 0.9144
        return x
    
    elif x == 'in':
        x = 0.0254
        return x
    
    else:
        x = 1
        return x

def miles(x):
    x = float(x / 1609.34)
    return x

def yards (x):
    x = float(x / 0.9144)
    return x

def inches(x):
    x = float(x / 0.0254)
    return x

def feet(x):
    x = float(x / 0.3048)
    return x

def kilometers(x):
    x = float(x / 1000)
    return x

def convert_output(x):
    if x == 'km':
        return kilometers(y)
                
    elif x == 'mi':
        return miles(y)

    elif x == 'yd':
        return yards(y)
    
    elif x == 'ft':
        return feet(y)

    elif x == 'in':
        return inches(y)

    else:
        return x


def main():
    while True:
        unit_from = input('\nWhat is the unit you wish to convert from \n[mi] miles, [km] kilometers, [yd] yards, [m] meters, [ft] feet or [in] inches? \nPlease enter the appropriate letter: ')
        
        if unit_from not in ('mi','km','yd','m','ft','in'):
            print('Please only enter \'mi\', \'km\',\'yd\',\'m\',\'ft\', or \'in\'.')
        else:
            break
    
    while True:
        unit_to = input('\nWhat is the unit you wish to convert to \n[mi] miles, [km] kilometers, [yd] yards, [m] meters, [ft] feet or [in] inches? \nPlease enter the appropriate letter: ')

        if unit_to not in ('mi,','km','yd','m','ft','in'):
            print('Please only enter \'mi\', \'km\',\'yd\',\'m\',\'ft\', or \'in\'.')
        else:
            break
  
    distance = float(input('\nPlease enter the distance: '))
    
    x = float(meters(unit_from))
    
    y = distance * x

    print(f'{str(distance)} {str(unit_from)} equals {str(convert_output(x))} {str(unit_to)}')
main()