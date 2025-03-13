import json

FILE_NAME = "student_db.json"

def load_data():
    """Loads student data from a JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    """Saves student data to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def calculate_gpa(grades):
    """Calculates GPA based on letter grades."""
    grade_points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
    total_points = sum(grade_points.get(grade, 0) for grade in grades)
    return round(total_points / len(grades), 2) if grades else 0

def add_student():
    """Allows user to add a new student record."""
    data = load_data()
    name = input("Enter Student Name: ").title()
    
    if name in data:
        print("❌ Student already exists!")
        return
    
    num_courses = int(input("Enter the number of courses: "))
    courses = {}
    
    for _ in range(num_courses):
        course = input("Enter course name: ").title()
        grade = input("Enter grade (A-F): ").upper()
        courses[course] = grade
    
    gpa = calculate_gpa(courses.values())
    data[name] = {"courses": courses, "GPA": gpa}
    
    save_data(data)
    print(f"✅ Student {name} added successfully!")

def view_students():
    """Displays all student records."""
    data = load_data()
    if not data:
        print("⚠️ No student records found!")
        return
    
    for name, details in data.items():
        print(f"\n🎓 {name} | GPA: {details['GPA']}")
        for course, grade in details["courses"].items():
            print(f"   📚 {course}: {grade}")

def search_student():
    """Searches for a specific student's report card."""
    data = load_data()
    name = input("Enter Student Name to Search: ").title()
    
    if name in data:
        print(f"\n🎓 {name} | GPA: {data[name]['GPA']}")
        for course, grade in data[name]["courses"].items():
            print(f"   📚 {course}: {grade}")
    else:
        print("❌ Student not found!")

def update_student():
    """Updates a student's grades."""
    data = load_data()
    name = input("Enter Student Name to Update: ").title()
    
    if name in data:
        print(f"🔄 Updating {name}'s record...")
        for course in list(data[name]["courses"].keys()):
            new_grade = input(f"Enter new grade for {course} (A-F): ").upper()
            data[name]["courses"][course] = new_grade
        
        data[name]["GPA"] = calculate_gpa(data[name]["courses"].values())
        save_data(data)
        print(f"✅ {name}'s record updated successfully!")
    else:
        print("❌ Student not found!")

def delete_student():
    """Deletes a student's record."""
    data = load_data()
    name = input("Enter Student Name to Delete: ").title()
    
    if name in data:
        del data[name]
        save_data(data)
        print(f"🗑️ {name}'s record deleted successfully!")
    else:
        print("❌ Student not found!")