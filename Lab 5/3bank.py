class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def details(self):
        print("Account_Holder=",self.account_holder)
        print("Account_Number=",self.account_number)
        print("Balance=",self.balance)
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
        print(f"The current balance is {self.balance}")

b1=BankAccount("Shriyon",1234,1000)
b1.details()
b1.deposit(1000)
b1.withdraw(500)
b1.show_balance()
b1.details()

