class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)

    def check_balance(self):
        print(f'Your current balance is ${self.balance}')

    def deposit(self, deposit_amount):
        self.balance = self.balance + float(deposit_amount)
        print(f'Balance after deposit is ${self.balance}')

    def check_withdrawel(self, withdrawel_amount):
        if withdrawel_amount > self.balance:
            return False

        else:
            return True

    def withdrawel(self, withdrawel_amount):
            self.balance = self.balance - withdrawel_amount
                
    def interest_calc(self):
        self.balance = self.balance + (self.balance * 0.001)

def main():
    account1 = ATM('John Doe', '321456', '200.00')

    while True:

        user_input = int(input('Weclome to Mr. Moneybags Bank.\nWhat would you like to do today?\nPlease enter number corresponding to the following\n1. Check your Balance?\n2. Make a deposit?\n3. Make a withdrawel?\n(1-3): '))

        if user_input == 1:
            account1.check_balance()
        elif user_input == 2:
            deposit_amount = float(input('How much would you like to deposit?: '))
            account1.deposit(deposit_amount)
        elif user_input == 3:
            withdrawel_amount = float(input('How much would you like to withdraw?: '))
            if account1.check_withdrawel(withdrawel_amount) == True:
                account1.withdrawel(withdrawel_amount)
                account1.check_balance()
            else:
                print('Insufficient funds to complete transaction.')

        else:
            print('Please only enter 1 - 3.')
        
        repeat_input = input('Would you like to make another transaction? Y/N: ')

        if repeat_input.lower() == 'y':
            continue
        elif repeat_input.lower() == 'n':
            break

main()