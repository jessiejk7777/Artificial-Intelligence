#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, time):
        self.tasks[task] = time
        print(f"Task '{task}' scheduled for {time}")

    def list_tasks(self):
        if self.tasks:
            print("Scheduled Tasks:")
            for task, time in self.tasks.items():
                print(f"- {task}: {time}")
        else:
            print("No tasks scheduled for today.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed from schedule.")
        else:
            print(f"No task named '{task}' found in schedule.")

    def clear_tasks(self):
        self.tasks = {}
        print("All tasks cleared.")

    def assist(self):
        print("How can I assist you today?")
        while True:
            command = input("Enter 'schedule' to add a task, 'list' to see scheduled tasks, 'remove' to remove a task, 'clear' to clear all tasks, or 'exit' to quit: ").lower()
            
            if command == 'schedule':
                task = input("Enter the task: ")
                time = input("Enter the time for the task (e.g., '14:00'): ")
                self.add_task(task, time)
            elif command == 'list':
                self.list_tasks()
            elif command == 'remove':
                task = input("Enter the task to remove: ")
                self.remove_task(task)
            elif command == 'clear':
                confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
                if confirm == 'yes':
                    self.clear_tasks()
                else:
                    print("Clear operation canceled.")
            elif command == 'exit':
                print("Goodbye!")
                break
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.assist()


# In[ ]:




