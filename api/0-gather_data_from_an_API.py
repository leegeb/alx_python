#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
        number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
