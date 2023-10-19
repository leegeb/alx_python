#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main":
    user_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    employee_id = user_data["id"]
    employee_name = user_data["name"]

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            completed_status = "True" if task["completed"] else "False"
            task_title = task["title"]
            writer.writerow([employee_id, employee_name,
                            completed_status, task_title])

    print(f"Data exported to {csv_filename}")
