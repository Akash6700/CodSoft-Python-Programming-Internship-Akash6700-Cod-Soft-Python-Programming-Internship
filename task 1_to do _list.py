import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {task['date']}")

def add_task(tasks, title):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({'title': title, 'date': date})
    print(f"Task '{title}' added on {date}")
    save_tasks(tasks)

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['title']}' removed.")
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '3':
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()