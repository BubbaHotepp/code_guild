def eval_func(x):
    return eval(x)

def main():
    user_input = input('Please enter a simple math problem to solve: ')

    print(f'{user_input} = {eval_func(user_input)}')

main()