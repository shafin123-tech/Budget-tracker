import json

## Add expenses
## total expenses
## show expenses and budget detail
## get balance
## use while loop for asking user for choice

filepath = 'budget_data_test.json'  # Define the path to your JSON file

expenses_list = []
# initial_budget = 1000
def add_expenses():
    description = input("write a info about purchese ")
    try:
        amount = int(input("write a amount "))
    except ValueError as e:
        print("Invalid amount. Please enter a numeric value.", e)

    expenses_list.append({"description": description, "amount": amount})
    print("expenses list", expenses_list)
    print("Expense added!")
    return  expenses_list

def total_expenses(expenses_list):
    total = 0
    for item in expenses_list:
        total = item["amount"] + total
    print("Total expenses so far: $",  total)
    return total

def get_balance(total_amount, budget):
    balance = budget - total_amount
    print(f"Remaining balance: ${balance}")
    return balance

def display_expenses_detail(expenses_list):
    if not expenses_list:
        print("No expenses recorded yet.")
    else:
        idx = 1  # Initialize an index counter
        for expense in expenses_list:
            print(f"{idx}. {expense['description']} - ${expense['amount']}")
            idx += 1  # Increment the index after each iteration

def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def load_budget_data_dict(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print("data", data)
        return {
            "initial_budget": data["initial_budget"],
            "expenses": data["expenses"]
        }
    except (FileNotFoundError, json.JSONDecodeError):
        return {"initial_budget": 0, "expenses": []}

def main():
    while True:
        print("\nWhat would you like to do? ")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Show total expenses")
        print("4. show the balance for the budget")
        print("5. load and show the expense on json file")

        budget_data = load_budget_data_dict(filepath)
        budget = budget_data["initial_budget"]
        if budget == 0:
            budget = int(input("write budget for expenses "))
        initial_budget = budget

        expenses = budget_data["expenses"]

        choice = input("enter option from the screen ")
        if choice == "1":
            exp =add_expenses()
            save = input("do you save in json file y/n")
            if save == "y":
                save_budget_data(filepath, initial_budget, exp)

        elif choice == "2":
            display_expenses_detail(expenses_list)
        elif choice == "3":
            total_expenses()

        elif choice =="4":
            get_balance(initial_budget)
        elif choice =="5":

            print("display expenses details")
            display_expenses_detail(expenses)
            print("Get total expensest")
            t= total_expenses(expenses)
            print("get balance")
            b =get_balance(t, initial_budget)
            print("remaing budget", b)



        elif choice =="6":
            print("exit")
            break

if __name__ == "__main__":
    main()
