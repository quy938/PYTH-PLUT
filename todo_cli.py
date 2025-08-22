
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to add")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
