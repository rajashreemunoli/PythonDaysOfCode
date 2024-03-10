#Create a class representing a simple bank account with deposit and withdraw methods
class bank_account:
    def __init__(self,account_number,customer_name,date_of_opening,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.date_of_opening=date_of_opening
        self.balance=balance
    
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
    
    def withdraw_amount(self,amount):
        if(amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Withdrawal successful.\nAccount balance: ${self.balance}")
    
    def deposit_amount(self,amount):
        self.balance+=amount
        print(f"Deposit successful.\nAccount balance: ${self.balance}")
    
    def account_details(self):
        print(f'Account number: {self.account_number}')
        print(f'Acounnt open date: {self.date_of_opening}')
        print(f'Account holder name: {self.customer_name}')
        print(f'Account balance: ${self.balance}')

account1=bank_account(1000,'Alex Rhodes','01-03-2023',3500)
account2=bank_account(1001,'Cindy Jones','05-13-2023',3000)
account3=bank_account(1002,'Kate Pears','12-01-2023',2000)

account1.account_details()
account2.account_details()
account3.account_details()

account1.withdraw_amount(500)
account2.deposit_amount(500)
account3.check_balance()