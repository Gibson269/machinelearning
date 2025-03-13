import to_do_list

def main():
    while True:
        print("\n📋 Personal TO-DO List")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Completed")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            to_do_list.add_task()
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.mark_task_completed()
        elif choice == "4":
            to_do_list.delete_task()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
