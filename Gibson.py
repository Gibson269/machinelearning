# Taking input scores
Eng = int(input("Please enter your English Exam Score (out of 100): "))
Math = int(input("Please enter your Math Exam Score (out of 100): "))
Chem = int(input("Please enter your Chemistry Exam Score (out of 100): "))

# Calculating average
Average = (Eng + Math + Chem) / 3

# Checking if the student failed any subject
if Eng < 40 or Math < 40 or Chem < 40:
    print("F - Fail (Failed in one or more subjects)")
else:
    # Assigning grades based on the average score
    if Average >= 90:
        print("A+ - Excellent")
    elif 80 <= Average < 90:
        print("A - Very Good")
    elif 70 <= Average < 80:
        print("B - Good")
    elif 60 <= Average < 70:
        print("C - Average")
    elif 50 <= Average < 60:
        print("D - Pass")
    else:
        print("F - Fail")
