import json
from datetime import datetime
import matplotlib.pyplot as plt  # Import Matplotlib for graphical reports

filepath = 'budget_data_test.json'  # Define the path to your JSON file

expenses_list = []


# Add expenses with categories
def add_expenses():
    description = input("Enter a description for the purchase: ")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Select category
    categories = ["food", "transport", "utilities", "entertainment", "others"]
    print("\nCategories: ")
    for index in range(len(categories)):
        print(f"{index + 1}. {categories[index]}")

    while True:
        try:
            category_choice = int(input("Select a category by number: "))
            if category_choice >= 1 and category_choice <= len(categories):
                category = categories[category_choice - 1]
                break
            else:
                print("Invalid selection. Choose a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Add current date for future analysis
    date = input("Enter date of the expense (YYYY-MM-DD) or leave blank for today: ")
    if date == "":
        date = str(datetime.today().date())  # Use today's date if none provided

    # Add the expense to the global expenses_list
    expenses_list.append({"description": description, "amount": amount, "category": category, "date": date})
    print("Expense added successfully!")
    return expenses_list


# Total expenses calculation
def total_expenses():
    total = 0
    for item in expenses_list:
        total += item["amount"]
    print("Total expenses so far: $", total)
    return total


# Calculate the remaining balance
def get_balance(total_expenses, budget):
    balance = budget - total_expenses
    print(f"Remaining balance: ${balance}")
    return balance


# Display all expenses
def display_expenses_detail():
    if len(expenses_list) == 0:
        print("No expenses recorded yet.")
    else:
        # Display the list without enumerate
        index = 1
        for expense in expenses_list:
            print(
                f"{index}. {expense['description']} - ${expense['amount']} | Category: {expense['category']} | Date: {expense['date']}")
            index += 1


# Reports by category with graphical pie chart
def report_by_category_graph():
    if len(expenses_list) == 0:
        print("No expenses recorded yet.")
        return

    # Calculate totals by category
    category_totals = {}
    for expense in expenses_list:
        category = expense["category"]
        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    # Plotting the pie chart
    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
    plt.show()


# Reports by month with graphical bar chart
def report_by_month_graph():
    if len(expenses_list) == 0:
        print("No expenses recorded yet.")
        return

    # Calculate totals by month
    month_totals = {}
    for expense in expenses_list:
        date_obj = datetime.strptime(expense["date"], "%Y-%m-%d")
        month = date_obj.strftime("%Y-%m")  # Extract year and month
        if month in month_totals:
            month_totals[month] += expense["amount"]
        else:
            month_totals[month] = expense["amount"]

    # Plotting the bar chart
    months = list(month_totals.keys())
    totals = list(month_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(months, totals, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Total Expenses ($)')
    plt.title('Expenses by Month')
    plt.xticks(rotation=45)  # Rotate month labels for readability
    plt.tight_layout()
    plt.show()


# Save budget data to a JSON file
def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    print("Budget data saved successfully!")


# Load budget data from a JSON file
def load_budget_data_dict(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return {
                "initial_budget": data.get("initial_budget", 0),
                "expenses": data.get("expenses", [])
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
        print("5. Graphical Report: Expenses by category (Pie Chart)")
        print("6. Graphical Report: Expenses by month (Bar Chart)")
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
            report_by_category_graph()

        elif choice == "6":
            report_by_month_graph()

        elif choice == "7":
            save_budget_data(filepath, initial_budget, expenses_list)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
