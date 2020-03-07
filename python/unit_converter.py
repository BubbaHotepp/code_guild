def main():

    feet = int(input('Please enter the distance in feet: '))

    def meter(x):
        conv = x * 0.3408
        return conv
    
    print(f'{feet} ft is {meter(feet)} meters.')
    
main()