import requests
import json

def get_all_employees_todo():
    all_employees_data = {}

    for employee_id in range(1, 11):
        employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data['username']
        
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todos_data = todos_response.json()

        tasks = []
        for task in todos_data:
            tasks.append({
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            })
        
        all_employees_data[str(employee_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file, indent=4)

    print("TODO list data for all employees saved in todo_all_employees.json.")

if __name__ == "__main__":
    get_all_employees_todo()
