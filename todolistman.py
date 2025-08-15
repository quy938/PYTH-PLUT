# Repository: python-todo-manager
# Description: A command-line to-do list manager.

tasks = []

def add_task(task):
    """Add a new task to the list."""
    tasks.append({"task": task, "completed": False})
    print(f"Task added: {task}")

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
