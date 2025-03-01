import json
import os
import argparse
from datetime import datetime

expenses_file = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file."""
    try:
        with open(expenses_file) as f:
            expenses = json.load(f)
    except FileNotFoundError:
        print(f"File {expenses_file} not found. Creating a new one.")
        expenses = []
        save_expenses(expenses)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {expenses_file}.")
        expenses = []
    return expenses


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(expenses_file, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expenses(description, amount):
    """Add a new expense."""
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added with ID: {description}, {amount}")


def update_expenses(expense_id, description, amount):
    """Update an existing expense."""
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["description"] = description
            expense["amount"] = amount
            save_expenses(expenses)
            print(f"Expense updated with ID: {expense_id}")
            return
    print(f"Expense ID {expense_id} not found")


def delete_expenses(expense_id):
    """Delete an expense."""
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print(f"Expense deleted with ID: {expense_id}")
            return
    print(f"Expense ID {expense_id} not found")


def list_expenses():
    """List all expenses."""
    expenses = load_expenses()
    print("ID       Date        Description     Amount")
    for expense in expenses:
        print(
            f"{expense['id']}    {expense['date']}   {expense['description']}        {expense['amount']}"
        )


def expense_summary(month=None):
    """Print a summary of expenses."""
    expenses = load_expenses()
    if month:
        expense = [
            exp
            for exp in expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d").month == month
        ]
        total = sum(exp["amount"] for exp in expense)
        print(f"Total expenses for {month} is {total}")
    else:
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total expenses is {total}")


def main():
    """Main function to parse arguments and perform actions."""
    parser = argparse.ArgumentParser(description="Expense Tracker")
    parser.add_argument(
        "action",
        type=str,
        choices=["add", "update", "delete", "list", "summary"],
        help="Action to perform",
    )
    parser.add_argument("--id", type=int, help="Expense ID")
    parser.add_argument("--description", type=str, help="Expense Description")
    parser.add_argument("--amount", type=float, help="Expense Amount")
    parser.add_argument("--month", type=int, help="Month")
    args = parser.parse_args()

    match args.action:
        case "add":
            if args.description and args.amount:
                add_expenses(args.description, args.amount)
            else:
                print("Description and amount are required for adding an expense.")
        case "update":
            if args.id and args.description and args.amount:
                update_expenses(args.id, args.description, args.amount)
            else:
                print(
                    "ID, description, and amount are required for updating an expense."
                )
        case "delete":
            if args.id:
                delete_expenses(args.id)
            else:
                print("ID is required for deleting an expense.")
        case "list":
            list_expenses()
        case "summary":
            expense_summary(args.month)


if __name__ == "__main__":
    if not os.path.exists(expenses_file):
        with open(expenses_file, "w") as f:
            json.dump([], f)

    main()
