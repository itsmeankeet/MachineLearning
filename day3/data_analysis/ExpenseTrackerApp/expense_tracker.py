import pandas as pd
columns = ['Date', 'Type', 'Amount', 'Category']
budget_df = pd.DataFrame(columns=columns)

def add_transaction(date, type, amount, category):
    date = date
    type = type
    amount = amount
    category = category
    new_entry = {'Date': date, 'Type': type, 'Amount': amount, 'Category': category}
    # budget_df = pd.concat([budget_df, pd.DataFrame([new_entry])], ignore_index=True)
    # This line adds a new row to budget_df at the next available index
    # len(budget_df) gives us the next empty row index since indices start at 0
    # .loc[] allows us to access and assign values by label/index
    # new_entry dictionary is assigned as the new row's values
    budget_df.loc[len(budget_df)] = new_entry
def analyze_budget():
    print("\nIncome\Expenses by Category:")
    category_totals = budget_df.groupby('Category')['Amount'].sum()
    for category, amount in category_totals.items():
        # This line checks if any transaction in the current category is an expense:
        # 1. budget_df['Category'] == category -> Creates a boolean mask for rows matching the current category
        # 2. budget_df[...]['Type'] -> Gets the 'Type' column for those matching rows
        # 3. .str.contains('Expense') -> Checks if any of those Types contain 'Expense'
        # 4. .any() -> Returns True if at least one row contains 'Expense'
        if budget_df[budget_df['Category'] == category]['Type'].str.contains('Expense').any():
            print("In Expense:\n")
            print(f"{category}: ${amount:.2f}")
        else:
            print("In Income:")
            print(f"{category}: ${amount:.2f}")
    print("Total Expense: ", budget_df[budget_df['Type'] == 'Expense']['Amount'].sum())
    print("Total Income: ", budget_df[budget_df['Type'] == 'Income']['Amount'].sum())
    budget_df.to_csv('budget_data.csv', index=False)

def main():
    while True:
        print("1. Add Transaction")
        print("2. Analyze Budget")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            type = input("Enter the type (Income/Expense): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            add_transaction(date, type, amount, category)
        elif choice == '2':
            analyze_budget()
        elif choice == '3':
            running = False
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            return 0

if __name__ == "__main__":
    main()

