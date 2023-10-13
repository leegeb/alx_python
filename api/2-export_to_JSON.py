""" student JSON output """
import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    username = user_data['username']

    tasks = []
    for task in todo_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    filename = f"{user_id}.json"
    with open(filename, 'w') as f:
        json.dump({user_id: tasks}, f)
