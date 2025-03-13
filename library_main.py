import library

def main():
    while True:
        print("\n📋 LIBRARY SHOPPING ")
        print("1️⃣ Add Books")
        print("2️⃣ Borrow Books")
        print("3️⃣ Return Books")
        print("4️⃣ View Availble Books")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_books()
        elif choice == "2":
            library.borrow_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.view_available_books()
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 



