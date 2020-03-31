class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)

    def check_balance(self):
        print(f'${self.balance}')

    def deposit(self, deposit_amount):
        self.balance = self.balance + float(deposit_amount)
       
    def check_withdrawel(self, withdrawel_amount):
        if withdrawel_amount > self.balance:
            return False

        else:
            return True

    def withdrawel(self, withdrawel_amount):
            self.balance = self.balance - withdrawel_amount
             

    def interest_calc(self):
        interest = self.balance * 0.001
        self.balance = self.balance + interest
        

def main():
    account1 = ATM('John Doe', '321456', '0.00')

    account1.check_balance()
        
    deposit_amount = 200.00
    account1.deposit(deposit_amount)
        
    withdrawel_amount = 50.00
    
    if account1.check_withdrawel(withdrawel_amount) == True:
                account1.withdrawel(withdrawel_amount, transactions)
    else:
        print('Insufficient funds.')
        
main()