def main():
    num_list = [5, 0, 8, 3, 4, 1, 6]
    run_sum = []
    x = 0

    for i in num_list:
        x += i
        run_sum.append(x)
        y = run_sum[-1]
        z = len(run_sum)
        print (f'Running sum is: {y}')
        print(f'Average is: {y/z}')

main()