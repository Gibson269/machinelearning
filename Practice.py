import json
from abc import ABC, abstractmethod

FILE_NAME = "employee_db.json"

def load_data():
    """Loads employee data from JSON file."""
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

def save_data(data):
    """Saves employee data to JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

class Employee(ABC):
    """Abstract class for Employee"""
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        """Abstract method for salary calculation."""
        pass  

    def save_employee(self):
        """Saves employee details to JSON file."""
        data = load_data()
        data.append({
            "ID": self.emp_id,
            "Name": self.name,
            "Department": self.department
        })
        save_data(data)
        print(f"✅ Employee {self.name} added successfully!")

class Fulltime(Employee):
    """Full-time Employee"""
    def __init__(self, name, emp_id, department, base_salary, allowance):
        super().__init__(name, emp_id, department)
        self.base_salary = float(base_salary)
        self.allowance = float(allowance)

    def calculate_salary(self):
        net_salary = self.base_salary + self.allowance - (0.2 * self.base_salary)
        return f"💰 {self.name}'s Net Salary: ${net_salary:.2f}"

class Parttime(Employee):
    """Part-time Employee"""
    def __init__(self, name, emp_id, department, hourly_rate, hours_worked):
        super().__init__(name, emp_id, department)
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)

    def calculate_salary(self):
        net_salary = self.hourly_rate * self.hours_worked
        return f"💰 {self.name}'s Net Salary: ${net_salary:.2f}"

class Intern(Employee):
    """Intern Employee"""
    def __init__(self, name, emp_id, department, stipend, bonus):
        super().__init__(name, emp_id, department)
        self.stipend = float(stipend)
        self.bonus = float(bonus)

    def calculate_salary(self):
        net_salary = self.stipend + self.bonus
        return f"💰 {self.name}'s Net Salary: ${net_salary:.2f}"

def add_employee():
    """Allows user to dynamically add an employee."""
    print("\n👥 Add a New Employee:")
    name = input("Enter Employee Name: ").title()
    emp_id = input("Enter Employee ID: ").upper()
    department = input("Enter Department: ").title()

    print("\nChoose Employee Type:")
    print("1️⃣ Full-Time")
    print("2️⃣ Part-Time")
    print("3️⃣ Intern")
    emp_type = input("Select an option (1-3): ")

    if emp_type == "1":
        base_salary = float(input("Enter Base Salary: "))
        allowance = float(input("Enter Allowance: "))
        employee = Fulltime(name, emp_id, department, base_salary, allowance)
    
    elif emp_type == "2":
        hourly_rate = float(input("Enter Hourly Rate: "))
        hours_worked = float(input("Enter Hours Worked: "))
        employee = Parttime(name, emp_id, department, hourly_rate, hours_worked)
    
    elif emp_type == "3":
        stipend = float(input("Enter Stipend: "))
        bonus = float(input("Enter Bonus: "))
        employee = Intern(name, emp_id, department, stipend, bonus)
    
    else:
        print("❌ Invalid selection. Please try again.")
        return

    employee.save_employee()
    print(employee.calculate_salary())

def view_employees():
    """Displays all employees from the database."""
    data = load_data()
    if not data:
        print("❌ No employees found in the system.")
        return

    print("\n📋 Employee List:")
    for index, emp in enumerate(data, start=1):
        print(f"{index}. {emp['Name']} (ID: {emp['ID']}, Department: {emp['Department']})")

def main():
    """Main function to run the employee system."""
    while True:
        print("\n🏢 EMPLOYEE MANAGEMENT SYSTEM")
        print("1️⃣ Add Employee")
        print("2️⃣ View Employees")
        print("3️⃣ Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
