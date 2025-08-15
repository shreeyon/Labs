import os
from datetime import datetime

CUSTOMERS_FILE = "customers.txt"
TRANSACTIONS_FILE = "transactions.txt"


def create_account():
    name = input("Customer name: ")
    account = input("Account number: ")
    balance = float(input("Initial balance: "))
    with open(CUSTOMERS_FILE, "a") as f:
        f.write(f"{name},{account},{balance}\n")
    log_transaction(account, "Open Account", balance)


def deposit(account, amount):
    update_balance(account, amount)
    log_transaction(account, "Deposit", amount)


def withdraw(account, amount):
    update_balance(account, -amount)
    log_transaction(account, "Withdrawal", amount)


def update_balance(account, amount):
    with open(CUSTOMERS_FILE, "r") as f:
        lines = f.readlines()
    with open(CUSTOMERS_FILE, "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if parts[1] == account:
                new_balance = float(parts[2]) + amount
                line = f"{parts[0]},{parts[1]},{new_balance}\n"
            f.write(line)


def log_transaction(account, type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRANSACTIONS_FILE, "a") as f:
        f.write(f"{timestamp},{account},{type},{amount}\n")


def main():
    while True:
        print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            account = input("Account number: ")
            amount = float(input("Amount: "))
            deposit(account, amount)
        elif choice == "3":
            account = input("Account number: ")
            amount = float(input("Amount: "))
            withdraw(account, amount)
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
