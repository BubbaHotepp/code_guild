# First version prints whether odd or even

def odd_even(x):
    
    if (x % 2) == 0:
        print (str(x) + ' is an even number.')
    else:
        print(str(x) + ' is an odd number.')

# Second version determines True False for even

def is_even(x):
    if (x % 2) == 0:
        print('True')
    else:
        print('False')

odd_even(6)

odd_even(3)

is_even(9)

is_even(8)


