expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total expenses")
    print("4. Filter by category")
    print("5. Delete expense")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("How much? "))
        category = input("What category? ")
        description = input("Description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

    elif choice == "2":
        print("\n====== Expenses ======")

        if not expenses:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(
                    f"{expense['amount']} € | {expense['category']} | {expense['description']}")

    elif choice == "3":
        print("\n====== Total expenses ======")
        total = 0
        for expense in expenses:
            total += expense['amount']

        print(f"Total: {total}€")

    elif choice == "4":
        print("\n====== Filter by category ======")
        category = input("Category: ")
        category_total = 0

        for expense in expenses:
            if expense['category'] == category:
                category_total += expense['amount']
                print(f"{expense['amount']} | {expense['description']}")

        print(f"Total expenses: {category_total}€")

    elif choice == "5":
        print("\n====== DELETE EXPENSE ======")
        for index, expense in enumerate(expenses):
            print(
                f"{index + 1}. {expense['amount']} € | {expense['category']} | {expense['description']}")
        try:
            expense_number = int(
                input("Which expense do you want to delete? "))

            if expense_number < 1 or expense_number > len(expenses):
                print("Invalid expense number!")
            else:
                expenses.pop(expense_number - 1)
                print("Expense deleted successfully!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
