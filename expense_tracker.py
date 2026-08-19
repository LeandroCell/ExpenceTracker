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
        for expense in expenses:
            print(f"{expense['amount']} € | {expense['category']} | {expense['description']}")

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
