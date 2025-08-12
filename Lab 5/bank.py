class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance


    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f" An amount of Rs.{amount} has been deposited succesfully")
        else:
            print("Deposit must be positive")

        

    def withdraw(self,amount):
         if (self.balance>amount):
            self.balance=self.balance-amount
            print(f"{amount} has been withdrawn successfully!")

         else:
             print("Insufficient Balance")


    def show_balance(self):
        print(f"The remaining balance is {self.balance}")

    
bank_details=BankAccount("Shreeyon Nepal",55577123,100000)
bank_details.deposit(50000)
bank_details.withdraw(80000)
bank_details.show_balance()