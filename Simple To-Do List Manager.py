# Repository: python-todo-manager


tasks = []

def add_task(task, priority="Low"):
    """Add a new task with priority."""
    tasks.append({"task": task, "priority": priority, "completed": False})
    print(f"Task added: {task} (Priority: {priority})")

def list_tasks():
    """List all tasks sorted by priority."""
    if not tasks:
        print("No tasks found.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: ["High", "Medium", "Low"].index(x["priority"]))
    for i, task in enumerate(sorted_tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. [{status}] {task['task']} (Priority: {task['priority']})")

# Example usage
add_task("Learn Python", "High")
add_task("Buy groceries", "Medium")
list_tasks()
