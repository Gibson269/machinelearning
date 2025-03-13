# Dictionary to store student course and grades
student_data = {}

# Dictionary mapping letter grades to GPA points
grade_points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

# Counter to limit number of courses
count = 0  

while count < 3:  # Limits input to 3 courses
    course = input("Enter your Course: ").strip().title()  # Clean user input
    grade = input("Enter your corresponding grade (A-F): ").strip().upper()  

    # Validate grade input
    if grade in grade_points:  
        student_data[course] = grade_points[grade]  # Store numerical grade
        count += 1  # Increment counter
    else:
        print("Invalid grade! Please enter a valid grade (A-F).")

# Display student courses and grades
print("\nStudent Course and Grades:", student_data)

# Calculate GPA
if student_data:  # Ensure there's valid data
    total_points = sum(student_data.values())  # Sum of grade points
    gpa = total_points / len(student_data)  # Compute average GPA
    print("\nYour GPA score is:", round(gpa, 2))  # Display rounded GPA
else:
    print("\nNo valid courses entered. Cannot calculate GPA.")
