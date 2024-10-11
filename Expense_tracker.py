import json

## Add expenses
## total expenses
## show expenses and budget detail
## get balance
## use while loop for asking user for choice

filepath = 'budget_data_test.json'
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

def total_expenses():
    total = 0
    for item in expenses_list:
        total = item["amount"] + total
    print("Total expenses so far: $",  total)
    return total

def get_balance(total_amount, budget):
    balance = budget - total_amount
    print(f"Remaining balance: ${balance}")
    return balance

def display_expenses_detail():
    if not expenses_list:
        print("No expenses recorded yet.")
    else:
        idx = 1  # Initialize an index counter
        for expense in expenses_list:
            print(f"{idx}. {expense['description']} - ${expense['amount']}")
            idx += 1  # Increment the index after each iteration

# Remove an expense
def remove_expense():
    display_expenses_detail()
    try:
        idx = int(input("Enter the number of the expense to remove: ")) - 1
        if idx < 0 or idx >= len(expenses_list):
            print("Invalid expense number.")
            return
        expenses_list.pop(idx)
        print("Expense removed successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

def edit_expense():
    display_expenses_detail()
    try:
        idx = int(input("Enter the number of the expense to edit: ")) - 1  # Get index to edit (zero-based)
        if idx < 0 or idx >= len(expenses_list):  # Validate index range
            print("Invalid expense number.")
            return
        description = input("Enter the new description: ")
        amount = float(input("Enter the new amount: "))
        expenses_list[idx] = {"description": description, "amount": amount}
        print("Expense updated successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

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
    budget_data = load_budget_data_dict(filepath)
    initial_budget = budget_data["initial_budget"]
    global expenses_list
    expenses_list = budget_data["expenses"]

    if initial_budget == 0:
        while True:
            try:
                initial_budget = float(input("Enter the budget: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the budget.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show all expenses")
        print("3. Show total expenses")
        print("4. Show remaining budget")
        print("5. Edit an expense")
        print("6. Remove an expense")
        print("7. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses()
            save_budget_data(filepath, initial_budget, expenses_list)

        elif choice == "2":
            display_expenses_detail()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            total = total_expenses()
            get_balance(total, initial_budget)

        elif choice == "5":
            edit_expense()
            save_budget_data(filepath, initial_budget, expenses_list)

        elif choice == "6":
            remove_expense()
            save_budget_data(filepath, initial_budget, expenses_list)

        elif choice == "7":
            save_budget_data(filepath, initial_budget, expenses_list)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
