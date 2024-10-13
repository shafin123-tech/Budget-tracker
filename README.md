Expense Tracker with Categories and Graphical Reports
This is a simple Expense Tracker application written in Python that allows users to track their expenses with categories, generate reports, and visualize their spending habits using graphical reports like pie charts and bar charts. The program saves and loads data using JSON files, allowing users to persist their expense history.

Features
Add Expenses: Record expenses with a description, amount, category, and date.
Expense Categories: Assign expenses to predefined categories (e.g., food, transport, utilities).
Display Expenses: Show a detailed list of all expenses.
Total Expenses: Calculate the total amount spent.
Balance Calculation: Calculate the remaining budget based on the initial budget.
Graphical Reports:
Pie Chart: Visualize expenses by category.
Bar Chart: Compare total expenses month by month.
Save and Load: Save expenses to a JSON file and load them on subsequent runs.
Installation
Clone the Repository:

If you haven't already cloned the repository, run this command in your terminal:

bash
Copy code
git clone https://github.com/your-username/expense-tracker.git
Navigate to the Project Directory:

bash
Copy code
cd expense-tracker
Install Required Libraries:

Install the dependencies using pip:

bash
Copy code
pip install matplotlib
matplotlib is used for generating the graphical reports in the form of pie and bar charts.

Run the Application:

To run the expense tracker, simply execute the Python file:

bash
Copy code
python expense_tracker.py
How to Use
Enter the Budget: When you first run the program, you'll be prompted to enter your initial budget.

Add an Expense:

Choose option 1 to add an expense.
You will be asked to provide a description, amount, and select a category.
The expense is then stored with the current date.
Show Expenses:

Choose option 2 to display all your expenses along with the category and date.
Show Total Expenses:

Choose option 3 to calculate and display the total of all recorded expenses.
Show Remaining Balance:

Choose option 4 to see how much of your budget is left after subtracting your total expenses.
Graphical Reports:

Choose option 5 to view a Pie Chart showing the total expenses by category.
Choose option 6 to view a Bar Chart comparing expenses by month.
Save and Exit:

Choose option 7 to save your expense data to a JSON file and exit the program.
Example Usage
markdown
Copy code
What would you like to do?
1. Add an expense
2. Show all expenses
3. Show total expenses
4. Show remaining budget
5. Graphical Report: Expenses by category (Pie Chart)
6. Graphical Report: Expenses by month (Bar Chart)
7. Save and Exit
Data Persistence
File Storage:
All your expenses and initial budget are saved to a file (budget_data_test.json) after you exit.
The next time you run the program, it will automatically load the saved data from this file.
Contributing
Feel free to fork this repository and make your own modifications. Pull requests are welcome!

License
This project is licensed under the MIT License.
