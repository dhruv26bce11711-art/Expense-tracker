expenses = [] 


#  options 
def show_options(): 
    print("\n" + "=" * 40) 
    print("        SMART EXPENSE TRACKER") 
    print("=" * 40) 
    print("1. Add Expense") 
    print("2. View All Expenses") 
    print("3. View Total Expenses") 
    print("4. View Expenses by Category") 
    print("5. Search Expense") 
    print("6. Show Highest Expense") 
    print("7. Monthly Expense Summary") 
    print("8. Delete Expense") 
    print("9. Exit") 
    print("=" * 40) 


# addng of expenses 
def add_expense(): 
    print("\n---------- Add Expense ----------") 

    date = input("Enter the date (YYYY-MM-DD): ").strip() 

    if date == "": 
        print("Date cannot be empty.") 
        return 

    description = input("What did you spend money on? ").strip() 

    if description == "": 
        print("Please enter a description.") 
        return 


    print("\nChoose a category:") 
    print("1. Food") 
    print("2. Transport") 
    print("3. Shopping") 
    print("4. Education") 
    print("5. Bills") 
    print("6. Entertainment") 
    print("7. Other") 

    category_choice = input("Enter your choice: ").strip() 

    categories = { 
        "1": "Food", 
        "2": "Transport", 
        "3": "Shopping", 
        "4": "Education", 
        "5": "Bills", 
        "6": "Entertainment", 
        "7": "Other" 
    } 

    if category_choice not in categories: 
        print("Invalid category. Expense was not added.") 
        return 

    category = categories[category_choice] 

    # Take the amount and make sure it is valid 
    try: 
        amount = float(input("Enter amount (₹): ")) 

        if amount <= 0: 
            print("Amount should be greater than 0.") 
            return 

    except ValueError: 
        print("Please enter a valid amount.") 
        return 

    expense = { 
        "date": date, 
        "description": description, 
        "category": category, 
        "amount": amount 
    } 

    expenses.append(expense) 

    print("\nExpense added successfully!") 
    print("-" * 35) 
    print("Date       :", date) 
    print("Description:", description) 
    print("Category   :", category) 
    print(f"Amount     : ₹{amount:.2f}") 
    print("-" * 35) 


# Display all the expenses 
def view_moneyspent(): 
    if len(expenses) == 0: 
        print("\nYou haven't added any expenses yet.") 
        return 

    print("\n========== ALL EXPENSES ==========") 

    for i, expense in enumerate(expenses, start=1): 
        print(f"\nExpense {i}") 
        print("-" * 35) 
        print("Date       :", expense["date"]) 
        print("Description:", expense["description"]) 
        print("Category   :", expense["category"]) 
        print(f"Amount     : ₹{expense['amount']:.2f}") 

    print("\n" + "=" * 35) 


# Calculate the total amount spent 
def total_moneyspent(): 
    if len(expenses) == 0: 
        print("\nNo expenses have been added yet.") 
        return 

    total = 0 

    for expense in expenses: 
        total += expense["amount"] 

    print("\n========== TOTAL EXPENSE ==========") 
    print(f"You have spent a total of ₹{total:.2f}") 
    print("=" * 35) 


# money spent on each category 
def category_moneyspent(): 
    if len(expenses) == 0: 
        print("\nNo expenses have been added yet.") 
        return 

    category_totals = {} 

    for expense in expenses: 
        category = expense["category"] 
        amount = expense["amount"] 

        if category in category_totals: 
            category_totals[category] += amount 
        else: 
            category_totals[category] = amount 

    print("\n======= EXPENSE BY CATEGORY =======") 

    for category, amount in category_totals.items(): 
        print(f"{category:<18} ₹{amount:.2f}") 

    print("=" * 35) 


# Search for an expense by description or category 
def search_expense(): 
    if len(expenses) == 0: 
        print("\nNo expenses have been added yet.") 
        return 

    search = input( 
        "\nEnter something to search (description/category): " 
    ).strip().lower() 

    found = False 

    print("\n========== SEARCH RESULTS ==========") 

    for i, expense in enumerate(expenses, start=1): 

        description = expense["description"].lower() 
        category = expense["category"].lower() 

        if search in description or search in category: 

            print(f"\nExpense {i}") 
            print("-" * 35) 
            print("Date       :", expense["date"]) 
            print("Description:", expense["description"]) 
            print("Category   :", expense["category"]) 
            print(f"Amount     : ₹{expense['amount']:.2f}") 

            found = True 

    if not found: 
        print("Sorry, no matching expense was found.") 

    print("=" * 35) 


# Find the expense with the highest amount 
def highest_amountspent(): 
    if len(expenses) == 0: 
        print("\nNo expenses have been added yet.") 
        return 

    highest = expenses[0] 

    for expense in expenses: 
        if expense["amount"] > highest["amount"]: 
            highest = expense 

    print("\n========= HIGHEST EXPENSE =========") 
    print("Date       :", highest["date"]) 
    print("Description:", highest["description"]) 
    print("Category   :", highest["category"]) 
    print(f"Amount     : ₹{highest['amount']:.2f}") 
    print("=" * 35) 


# Show expenses for a particular month 
def monthly_spent(): 
    if len(expenses) == 0: 
        print("\nNo expenses have been added yet.") 
        return 

    month = input( 
        "\nEnter the month you want to check (YYYY-MM): " 
    ).strip() 

    total = 0 
    count = 0 

    print("\n========= MONTHLY SUMMARY =========") 

    for expense in expenses: 

        if expense["date"].startswith(month): 

            print( 
                f"{expense['date']} | " 
                f"{expense['description']} | " 
                f"{expense['category']} | " 
                f"₹{expense['amount']:.2f}" 
            ) 

            total += expense["amount"] 
            count += 1 

    if count == 0: 
        print("No expenses were found for this month.") 

    else: 

        print("-" * 40) 
        print("Number of expenses:", count) 
        print(f"Total spent      : ₹{total:.2f}") 

        average = total / count 
        print(f"Average expense  : ₹{average:.2f}") 

    print("=" * 40) 


# Delete an expense from the list 
def delete_expense(): 
    if len(expenses) == 0: 
        print("\nThere are no expenses to delete.") 
        return 

    view_moneyspent() 

    try: 
        number = int(input("\nEnter the expense number you want to delete: ")) 

        if number < 1 or number > len(expenses): 
            print("That expense number does not exist.") 
            return 

        removed_expense = expenses.pop(number - 1) 

        print("\nExpense deleted successfully!") 
        print( 
            f"Removed: {removed_expense['description']} " 
            f"- ₹{removed_expense['amount']:.2f}" 
        ) 

    except ValueError: 
        print("Please enter a valid expense number.") 


# Main part of the program 
print("\n" + "=" * 40) 
print("       WELCOME TO EXPENSE TRACKER") 
print("=" * 40) 

while True: 

    show_options() 

    choice = input("Enter your choice: ").strip() 

    if choice == "1": 
        add_expense() 

    elif choice == "2": 
        view_moneyspent() 

    elif choice == "3": 
        total_moneyspent() 

    elif choice == "4": 
        category_moneyspent() 

    elif choice == "5": 
        search_expense() 

    elif choice == "6": 
        highest_amountspent() 

    elif choice == "7": 
        monthly_spent() 

    elif choice == "8": 
        delete_expense() 

    elif choice == "9": 
        print("\n" + "=" * 40) 
        print("Thank you for using Expense Tracker!") 
        print("Have a great day!") 
        print("=" * 40) 
        break 

    else: 
        print("\nInvalid choice.") 
        print("Please select a number from 1 to 9.") 
