import json

TASK_DB = "task_db.json"

def load_data():
    """Loads tasks from JSON file."""
    try:
        with open(TASK_DB, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Now using a list to store tasks

def save_data(data):
    """Saves tasks to JSON file."""
    with open(TASK_DB, "w") as file:
        json.dump(data, file, indent=4)

def add_task():
    """Allows users to add a task."""
    data = load_data()  # Load existing tasks

    try:
        task_count = int(input("How many tasks do you have planned for today? "))
        for _ in range(task_count):
            task = input("Enter your task: ").title()
            deadline = input("Enter your deadline (e.g., 5PM, Tomorrow): ").upper()
            
            # Append task as a dictionary
            data.append({"task": task, "deadline": deadline, "completed": False})
            print(f"✅ Task '{task}' added successfully!")

        save_data(data)  # Save updated data
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

def view_tasks():
    """Displays all tasks."""
    data = load_data()
    
    if not data:
        print("⚠️ No tasks found! Start adding some.")
        return
    
    print("\n📌 Your To-Do List:")
    for index, task in enumerate(data, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{index}. {task['task']} - Deadline: {task['deadline']} [{status}]")

def mark_task_completed():
    """Marks a task as completed."""
    data = load_data()

    if not data:
        print("⚠️ No tasks available!")
        return

    view_tasks()  # Show current tasks
    try:
        task_index = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(data):
            data[task_index]["completed"] = True
            save_data(data)
            print(f"✅ Task '{data[task_index]['task']}' marked as completed!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    """Deletes a task."""
    data = load_data()

    if not data:
        print("⚠️ No tasks to delete!")
        return

    view_tasks()  # Show current tasks
    try:
        task_index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= task_index < len(data):
            removed_task = data.pop(task_index)  # Remove the selected task
            save_data(data)
            print(f"🗑️ Task '{removed_task['task']}' deleted successfully!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")
