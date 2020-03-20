def main():
    num_list = []
    run_sum = []
    num_input = ''    
    x = 0

    while num_input != 'done':
        
        num_input = input('Please enter a number or \'done\' if you are finished: ')
        
        if num_input != 'done':
            num_list.append(int(num_input))
            print(num_list)
    
    for i in num_list:
        x += i
        run_sum.append(x)
        y = run_sum[-1]
        z = len(run_sum)
        print ('Running sum is: ' + str(y))
        print('Average is: ' + str(y/z))

main()