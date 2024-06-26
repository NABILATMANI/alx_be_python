# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task."

# Modify the reminder based on the time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Provide a customized reminder using match-case
match priority:
    case "high":
        print(f"Reminder: {reminder}")
    case "medium":
        print(f"Reminder: {reminder}")
    case "low":
        print(f"Reminder: {reminder}. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level provided.")
