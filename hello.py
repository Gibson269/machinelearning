## Create a list to store and calculate average grades for students
count = 0  # Counter to track number of inputs
grades = {}  # Dictionary to store course: score

while count < 5:  # Ensure only 5 inputs
    course = input("Enter your course: ")
    score = float(input("Enter your corresponding score: "))  # Convert score to float

    grades[course] = score  # Store course and score in dictionary
    count += 1  # Increment counter

print("\nStudent Grades:")
for course, score in grades.items():
    print(f"{course}: {score}")

# Calculate and display average score
average_score = sum(grades.values()) / len(grades)
print(f"\nAverage Score: {average_score:.2f}")