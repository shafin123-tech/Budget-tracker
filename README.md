# Expense Tracker with Categories and Graphical Reports

This is a simple **Expense Tracker** application written in Python that allows users to track their expenses with categories, generate reports, and visualize their spending habits using graphical reports like pie charts and bar charts. The program saves and loads data using JSON files, allowing users to persist their expense history.

## Features
- **Add Expenses**: Record expenses with a description, amount, category, and date.
- **Expense Categories**: Assign expenses to predefined categories (e.g., food, transport, utilities).
- **Display Expenses**: Show a detailed list of all expenses.
- **Total Expenses**: Calculate the total amount spent.
- **Balance Calculation**: Calculate the remaining budget based on the initial budget.
- **Graphical Reports**: 
  - **Pie Chart**: Visualize expenses by category.
  - **Bar Chart**: Compare total expenses month by month.
- **Save and Load**: Save expenses to a JSON file and load them on subsequent runs.

## Installation

### Clone the Repository:
If you haven't already cloned the repository, run this command in your terminal:

```bash
git clone https://github.com/your-username/expense-tracker.git
```
## Navigate to the Project Directory:
```bash
cd expense-tracker
```

## Install the dependencies using pip:

```bash
pip install matplotlib
```
matplotlib is used for generating the graphical reports in the form of pie and bar charts.
Run the Application
## To run the expense tracker, simply execute the Python file:
```bash
python expense_tracker.py
```
- **Data Persistence**
- **File Storage**:

All your expenses and initial budget are saved to a file (budget_data_test.json) after you exit.
The next time you run the program, it will automatically load the saved data from this file.
Contributing
Feel free to fork this repository and make your own modifications. Pull requests are welcome!

## License
This project is licensed under the MIT License.
