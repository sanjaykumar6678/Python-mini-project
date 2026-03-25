# Mini Project 7: Bank Account System
# Simulate bank operations.

account = {}

def create_account():
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))
    account["name"] = name
    account["balance"] = balance
    print("Account Created")

def deposit():
    amount = float(input("Enter Amount to Deposit: "))
    account["balance"] += amount
    print("Amount Deposited")

def withdraw():
    amount = float(input("Enter Amount to Withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")

def check_balance():
    print("Current Balance:", account.get("balance", 0))


# Menu

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Balance 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")