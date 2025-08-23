# Description: A command-line to-do list manager.

tasks = []

def add_task(task, due_date=None):
    tasks.append({"task": task, "completed": False, "due_date": due_date})
    print(f"Task added: {task} (Due: {due_date or 'No due date'})")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. {task['task']} [{status}]")

def mark_completed(index):
    """Mark a task as completed."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task marked as completed: {tasks[index]['task']}")
    else:
        print("Invalid task index.")

# Example usage
add_task("Learn Python")
add_task("Build a project")
list_tasks()
mark_completed(0)
list_tasks()
