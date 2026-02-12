print("Welcome to the Daily Expense Tracker!")


print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    choice = input("")
   
    if choice == "1":
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")
    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
                total = sum(expenses)
                average = total / len(expenses)
                print("Total expense:",total)
                print("Average expense:",average)

    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")

    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
