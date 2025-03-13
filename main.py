import Student

def main():
    while True:
        print("\n🎓 Student Report Card System 🎓")
        print("1️⃣ Add Student")
        print("2️⃣ View All Students")
        print("3️⃣ Search Student")
        print("4️⃣ Update Student")
        print("5️⃣ Delete Student")
        print("6️⃣ Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            Student.add_student()
        elif choice == "2":
            Student.view_students()
        elif choice == "3":
            Student.search_student()
        elif choice == "4":
            Student.update_student()
        elif choice == "5":
            Student.delete_student()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()