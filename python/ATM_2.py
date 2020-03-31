class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)

    def check_balance(self):
        print(self.balance)

    def deposit(self, deposit_amount, transactions):
        self.balance = self.balance + float(deposit_amount)
        transactions.append(f'Depost = {deposit_amount}')

    def check_withdrawel(self, withdrawel_amount):
        if withdrawel_amount > self.balance:
            return False

        else:
            return True

    def withdrawel(self, withdrawel_amount, transactions):
            self.balance = self.balance - withdrawel_amount
            transactions.append(f'Withdrawel = {withdrawel_amount}') 

    def interest_calc(self, transactions):
        interest = self.balance * 0.001
        self.balance = self.balance + interest
        transactions.append(f'Interest applied = {interest}')

def main():
    account1 = ATM('John Doe', '321456', '0.00')
    transactions = []

    account1.check_balance()
        
    deposit_amount = 1000.51
    account1.deposit(deposit_amount, transactions)
        
    withdrawel_amount = 500.00
    if account1.check_withdrawel(withdrawel_amount) == True:
        account1.withdrawel(withdrawel_amount, transactions)
        account1.check_balance()
    
    else:
        print('Insufficient funds to complete transaction.')
        
    print(transactions)
    
main()