#!/usr/bin/python3
import requests
import sys
import csv


def get_employee_data(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    csv_data = []
    for task in todo_data:
        task_completed_status = "Completed" if task['completed'] else "Not Completed"
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

    with open(f'{user_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        writer.writerows(csv_data)

    print(f'CSV file "{user_id}.csv" has been created successfully.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_data(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
