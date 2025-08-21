class Bank:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,new_balance):
        self.balance+=new_balance
        print(f"{new_balance} is credited")

    def withdraw(self,new_balance):
        if(self.balance>new_balance):
            self.balance-=new_balance
            print(f"{new_balance} is debited")
        else:
            print("Insufficient Balance")

    def show_details(self):
        print(f"Account Number={self.account_number}\nBalance={self.balance}")

b1=Bank(1234,1000)
b1.deposit(1000)
b1.withdraw(500)
b1.show_details()



