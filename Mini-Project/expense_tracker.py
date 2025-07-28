import csv
import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = 'expenses.csv'
FIELDNAMES = ['date', 'category', 'amount', 'description']

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent, Transport): ").capitalize()
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        })
    print("✅ Expense added.\n")

def read_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def report_total():
    expenses = read_expenses()
    total = sum(float(e['amount']) for e in expenses)
    print(f"\n💰 Total Expenses: ${total:.2f}")

def report_by_category():
    expenses = read_expenses()
    category_totals = defaultdict(float)
    for e in expenses:
        category_totals[e['category']] += float(e['amount'])
    print("\n📊 Expenses by Category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: ${amt:.2f}")

def report_monthly_summary():
    expenses = read_expenses()
    monthly_totals = defaultdict(float)
    for e in expenses:
        month = datetime.strptime(e['date'], '%Y-%m-%d').strftime('%Y-%m')
        monthly_totals[month] += float(e['amount'])
    print("\n🗓️ Monthly Summary:")
    for month, amt in sorted(monthly_totals.items()):
        print(f"  {month}: ${amt:.2f}")

def main():
    initialize_file()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Total Expenses")
        print("3. Show Expenses by Category")
        print("4. Show Monthly Summary")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            report_total()
        elif choice == '3':
            report_by_category()
        elif choice == '4':
            report_monthly_summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
