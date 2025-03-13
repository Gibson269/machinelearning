# Student Grade Management System
students = []  # List to store student names and grades

# Taking input for student records
while True:
    name = input("Enter student name (or type 'done' to stop): ")
    if name.lower() == "done":
        break  # Stop input when user types 'done'
    
    try:
        grade = float(input(f"Enter {name}'s grade: "))  # Ask for grade
        students.append([name, grade])  # Store as nested list
    except ValueError:
        print("Invalid grade! Please enter a valid number.")

# Display menu options for user
while True:
    print("\n📌 MENU OPTIONS:")
    print("1. Display all student records")
    print("2. Find the highest and lowest scores")
    print("3. Calculate and display the class average")
    print("4. Search for a student’s grade")
    print("5. Sort students by their grades (highest to lowest)")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n📌 Student Records:")
        for student in students:
            print(f"Name: {student[0]}, Grade: {student[1]}")

    elif choice == "2":
        if students:
            highest = max(students, key=lambda x: x[1])  # Find highest scorer
            lowest = min(students, key=lambda x: x[1])  # Find lowest scorer
            print(f"\n🏆 Highest Score: {highest[0]} - {highest[1]}")
            print(f"⚠️ Lowest Score: {lowest[0]} - {lowest[1]}")
        else:
            print("\nNo student records available.")

    elif choice == "3":
        if students:
            average = sum(student[1] for student in students) / len(students)
            print(f"\n📊 Class Average: {round(average, 2)}")
        else:
            print("\nNo student records available.")

    elif choice == "4":
        search_name = input("\nEnter the student’s name to search: ")
        found = [student for student in students if student[0].lower() == search_name.lower()]
        if found:
            print(f"{found[0][0]}'s Grade: {found[0][1]}")
        else:
            print("Student not found!")

    elif choice == "5":
        sorted_students = sorted(students, key=lambda x: x[1], reverse=True)  # Sort by grade
        print("\n📌 Students Sorted by Grades (Highest to Lowest):")
        for student in sorted_students:
            print(f"{student[0]} - {student[1]}")

    elif choice == "6":
        print("\nProgram Exited. Goodbye! 🚀")
        break

    else:
        print("\nInvalid choice! Please select a valid option.")
