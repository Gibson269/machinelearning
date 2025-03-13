import json
import os

FILE_NAME = "employees.json"

# ✅ Load employee data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Load JSON into Python list
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty

# ✅ Save employee data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)  # Store data in readable JSON format

# ✅ Add a new employee
def add_employee():
    data = load_data()  # Load current data

    emp_name = input("Enter employee name: ").title()
    emp_id = input("Enter employee ID: ").upper()
    emp_department = input("Enter department: ").title()
    
    try:
        emp_salary = float(input("Enter salary: "))  # Ensure valid numeric input
    except ValueError:
        print("⚠️ Invalid salary input. Must be a number!")
        return

    # Add new employee record
    data.append({
        "Employee Name": emp_name,
        "Employee ID": emp_id,
        "Department": emp_department,
        "Salary": emp_salary
    })

    save_data(data)  # Save to file
    print(f"✅ Employee '{emp_name}' added successfully!")

# ✅ View all employees
def view_employees():
    data = load_data()
    
    if not data:
        print("⚠️ No employees found.")
        return

    print("\n📋 Employee List:")
    for emp in data:
        print(f"🔹 Name: {emp['Employee Name']}, ID: {emp['Employee ID']}, Department: {emp['Department']}, Salary: ${emp['Salary']:,.2f}")

# ✅ Search for an employee by ID
def search_employee():
    data = load_data()
    
    if not data:
        print("⚠️ No employees found.")
        return

    emp_id = input("Enter Employee ID to search: ").upper()

    found = next((emp for emp in data if emp["Employee ID"] == emp_id), None)

    if found:
        print(f"\n🔍 Employee Found: {found}")
    else:
        print(f"❌ No employee found with ID '{emp_id}'.")

# ✅ Delete an employee by ID
def delete_employee():
    data = load_data()
    
    if not data:
        print("⚠️ No employees found.")
        return

    emp_id = input("Enter Employee ID to delete: ").upper()
    
    new_data = [emp for emp in data if emp["Employee ID"] != emp_id]  # Remove matching employee

    if len(new_data) == len(data):
        print(f"❌ No employee found with ID '{emp_id}'.")
    else:
        save_data(new_data)
        print(f"✅ Employee with ID '{emp_id}' deleted successfully!")

# ✅ Main menu function
def main():
    while True:
        print("\n📌 EMPLOYEE MANAGEMENT SYSTEM")
        print("1️⃣ Add Employee")
        print("2️⃣ View Employees")
        print("3️⃣ Search Employee")
        print("4️⃣ Delete Employee")
        print("5️⃣ Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("🚪 Exiting... Thank you!")
            break
        else:
            print("⚠️ Invalid choice, please try again!")

# ✅ Run the program
if __name__ == "__main__":
    main()
