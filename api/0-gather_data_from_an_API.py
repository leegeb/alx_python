#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    # Extract relevant information
    employee_name = user_data["name"]
    # Limit employee name to 18 characters
    truncated_name = employee_name[:18] if len(employee_name) > 18 else employee_name
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)

    # Print the required output format
    print(f"Employee {truncated_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")

