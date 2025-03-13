import json

LIBRARY_DB = "library_db.json"

def load_data():
    """Loads tasks from JSON file."""
    try:
        with open(LIBRARY_DB, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):  # Ensure data is a dictionary
                return {"books": []}  # Reset to proper structure
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"books": []}  # Default structure if file is missing or empty
    
def save_data(data):
    """Saves tasks to JSON file."""
    with open(LIBRARY_DB, "w") as file:
        json.dump(data, file, indent=4)

def add_books ():
    data=load_data() # Allows user to load data from JSON file

    try:
        entry_count=int(input("What is the number of books you want to add up ? "))  # takes the count for the book number to be entered

        for _ in range (entry_count):
            book_title = input ("Please enter the book title  -   ").title()
            book_author= input("Please kindly attached the author of the book  -  ").title()
            
             # Append new book entry
            data["books"].append({
                "title": book_title,
                "author": book_author,
                "available": True  # Track book availability
            })
        
        save_data(data)  # Save updated data
        print(f"✅ {entry_count} book(s) added successfully!")

    except ValueError:
        print("Input not accepted, please try again  ")


def borrow_book():
    """Allows users to borrow a book if available."""
    data = load_data()  # Load book records

    if not data["books"]:  # ✅ Check if library is empty
        print("❌ No books available in the library.")
        return

    book_title = input("Enter the book you want to borrow: ").title()

    for book in data["books"]:
        if book["title"] == book_title:
            if book["available"]:  # ✅ Check if book is available
                user_name = input("Enter your name: ").title()
                book["available"] = False  # Mark book as borrowed
                book["borrowed_by"] = user_name  # Track borrower
                save_data(data)  # Save updated data
                print(f"✅ {book_title} has been borrowed by {user_name}.")
                return  # ✅ Exit function after success
            else:
                print(f"❌ Sorry, {book_title} is already borrowed by {book.get('borrowed_by', 'someone else')}.")
                return  # ✅ Exit to prevent checking other books with the same title

    print("❌ Book not found in the library.")  # ✅ If no book matched, show this


def return_book():
    """Allows users to return a borrowed book."""
    data = load_data()  # Load book records

    book_title = input("Enter the book you want to return: ").title()

    for book in data["books"]:
        if book["title"] == book_title:
            if not book["available"]:  # Check if the book is borrowed
                book["available"] = True  # Mark as available
                book.pop("borrowed_by", None)  # Remove borrower's name
                save_data(data)  # Save changes
                print(f"✅ {book_title} has been returned successfully!")
                return  # Exit after successful return
            else:
                print(f"❌ {book_title} is already available in the library.")
                return

    print("❌ Book not found in the library.")

def view_available_books():
    """Displays a list of all available books with their authors."""
    data = load_data()  # Load book records

    available_books = [
        {"title": book["title"], "author": book["author"]}
        for book in data["books"] if book["available"]
    ]

    if available_books:
        print("\n📚 Available Books:")
        for index, book in enumerate(available_books, start=1):
            print(f"{index}. {book['title']} by {book['author']}")
    else:
        print("❌ No books are currently available for borrowing.")

    return available_books  # ✅ Returns a list of dictionaries







    






