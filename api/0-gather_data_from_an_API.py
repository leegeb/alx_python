#!/usr/bin/python3
import requests
import sys


def get_employee_todo_progress(employee_id):
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    print(
        f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
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
