
## Add expenses
## total expenses
## show expenses and budget detail
## get balance
## use while loop for asking user for choice

expenses_list = []
initial_budget = 1000
def add_expenses():
    description = input("write a info about purchese ")
    amount = int(input("write a amount "))
    expenses_list.append({"description": description, "amount": amount})
    print(expenses_list)

    return  expenses_list

def total_expenses():
    total = 0
    for item in expenses_list:
        total = item["amount"] + total
    print("total expenses",  total)
    return total

def get_balance(total_amount):
    balance = total_amount -1000
    return  balance

def display_expenses_detail():
    for i in expenses_list:
        print(f"info {i['description']}, amount -> {i['amount']}")


while True:
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. Show budget details")
    print("3. Show total expenses")
    print("4. show the balance for the budget")
    choice = input("enter option from the screen ")
    if choice == "1":
        add_expenses()
    elif choice == "2":
        display_expenses_detail()
    elif choice == "3":
        total_expenses()

    elif choice =="4":
        get_balance()
    elif choice =="4":
        print("exit")
        break


