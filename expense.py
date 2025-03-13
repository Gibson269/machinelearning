import json

FILE_NAME = "user_db.json"

def load_data():
    """Loads user data from a JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": 0, "expenses": {}}

def save_data(data):
    """Saves user data to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_income():
    """Allows user to add a new income record."""
    data = load_data()
    
    try:
        income = float(input("Enter your monthly income: "))
        data["income"] = income  # Store income properly
        save_data(data)
        print(f"✅ Income of ${income} added successfully!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

def add_expense():
    """Allows user to add categorized expenses."""
    data = load_data()

    try:
        food_expense = float(input("Enter your monthly expense on Food: $"))
        transport_expense = float(input("Enter your monthly expense on Transport: $"))
        bills_expense = float(input("Enter your monthly expense on Bills: $"))
        misc_expense = float(input("Enter your monthly expense on Miscellaneous: $"))

        total_expense = food_expense + transport_expense + bills_expense + misc_expense
        
        data["expenses"] = {
            "Food": food_expense,
            "Transport": transport_expense,
            "Bills": bills_expense,
            "Miscellaneous": misc_expense,
            "Total": total_expense
        }

        save_data(data)
        print(f"✅ Total expenses recorded: ${total_expense}")
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

def view_income():
    """Displays stored income."""
    data = load_data()
    print(f"💰 Your recorded income is: ${data['income']}")

def view_expenses():
    """Displays all expenses."""
    data = load_data()
    expenses = data.get("expenses", {})

    if not expenses:
        print("⚠️ No expenses recorded yet!")
        return

    print("\n📊 Expense Breakdown:")
    for category, amount in expenses.items():
        print(f"   - {category}: ${amount}")

def check_balance():
    """Calculates and displays remaining balance."""
    data = load_data()
    balance = data["income"] - data["expenses"].get("Total", 0)
    print(f"💵 Remaining Balance: ${balance}")
