import requests
import sys
import json

def get_employee_todo_progress(employee_id):
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file, indent=4)

    print(f"Employee {employee_name} TODO list progress saved in {employee_id}.json.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
