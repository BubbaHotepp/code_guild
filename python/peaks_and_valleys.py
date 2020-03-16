def peaks(x):
    
    y = 0
    z = []
    length = len(x) - 2
    
    while y < length:
    
        print(y)
        a = y + 1
        print(a)
        b = y + 2
        print(b)
    
        if x[y] < x[a]:
    
            if x[a] > x [b]:
    
                z.append((a))
                y += 1
    
            else:
                y += 1
    
        else:
            y +=1
    
    return z

def valleys(x):
    
    y = 0
    z = []
    length = len(x) - 2
    
    while y < length:
    
        a = y + 1
        b = y + 2
    
        if x[y] > x[(a)]:
    
            if x[(a)] < x[(b)]:
    
                z.append((a))
                y += 1
    
            else:
                y += 1
    
        else:
            y += 1
    
    return z

def peaks_and_valleys(x):
    
    a = peaks(x)
    b = valleys(x)
    c = a + b
    c.sort()
    
    return c

def main():
    
    data_set = (1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9)

    x = peaks(data_set)
    y = valleys(data_set)
    z = peaks_and_valleys(data_set)
    
    print(f'Peaks: {x}')
    print(f'Valleys: {y}')
    print(f'Peaks and Valleys: {z}')

main()