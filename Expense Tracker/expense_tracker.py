import datetime
import calendar
from expense import Expense  # Assuming `Expense` class is defined in `expense` module

def main():
    # Prompt user for their name
    user_name1 = input("What's Your Name: ")
    print(f"💸 Running {user_name1} Expense Tracker! 🤑")

    # File to store expenses
    expense_file_path = "expenses.csv"

    # Ask user for their budget
    budget = float(input("What's Your Budget: "))  # Convert budget to float

    # Get user input for expense
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read the file and summarize expenses
    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    # Prompt user for expense details
    expense_name = input("💰 Enter expense name: ")
    expense_amount = float(input("💵 Enter amount number: "))

    # List of expense categories
    expense_categories = ["🍔 Food", "🏠 Home", "💻 Work", "😜 Fun", "👑 Other"]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense  # Return the created expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense: Expense, expense_file_path):
    # Save expense to file
    with open(expense_file_path, "a", encoding="utf-8") as f:  # Specify encoding
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    # Read expenses from file and summarize
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:  # Specify encoding
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    # Calculate total spent by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # Print expenses by category
    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}") 

    # Calculate total spent
    total_spent = sum([expense.amount for expense in expenses])
    print(f"📉You've Spent ${total_spent:.2f}")

    # Calculate remaining budget
    remaining_budget = budget - total_spent
    print(f"💲 Budget Remaining: ${remaining_budget:.2f}")

    # Calculate remaining days in the month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    # Calculate daily budget
    daily_budget = remaining_budget / remaining_days
    print("\033[92m👉 Budget Per Day: ${:.2f} For {remaing_days}\033[0m".format(daily_budget))


if __name__ == "__main__":
    main()
