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
    elif x == 'm':
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


def main():
        
    unit_from = input('\nWhat is the unit you wish to convert from \n[mi] miles, [km] kilometers, [yd] yards, [m] meters, [ft] feet or [in] inches? \nPlease enter the appropriate letter: ')
    
    unit_to = input('\nWhat is the unit you wish to convert to \n[mi] miles, [km] kilometers, [yd] yards, [m] meters, [ft] feet or [in] inches? \nPlease enter the appropriate letter: ')
  
    distance = float(input('\nPlease enter the distance: '))
    
    x = float(meters(unit_from))
    
    y = distance * x

    if unit_to == 'km':

        output = kilometers(y)
                
    if unit_to == 'mi':

        output = miles(y)

    if unit_to == 'yd':
        
        output = yards(y)
    
    if unit_to == 'ft':

        output = feet(y)

    if unit_to == 'in':

        output = inches(y)

    if unit_to == 'm':

        output = x
    
    print(str(distance) + ' ' + str(unit_from) + ' equals ' + str(output) + ' ' + str(unit_to))
main()