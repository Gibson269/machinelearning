import expense

def main():
    while True:
        print("\n💰 Personal Budget Manager")
        print("1️⃣ Add Income")
        print("2️⃣ Add Expenses")
        print("3️⃣ View Income")
        print("4️⃣ View Expenses")
        print("5️⃣ Check Balance")
        print("6️⃣ Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            expense.add_income()
        elif choice == "2":
            expense.add_expense()
        elif choice == "3":
            expense.view_income()
        elif choice == "4":
            expense.view_expenses()
        elif choice == "5":
            expense.check_balance()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
