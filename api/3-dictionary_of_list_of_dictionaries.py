import json
import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

users = requests.get(USERS_URL).json()

todos = requests.get(TODOS_URL).json()

data = {}
for todo in todos:
    user_id = todo['userId']
    username = next(user['username'] for user in users if user['id'] == user_id)
    
    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        'username': username,
        'task': todo['title'],
        'completed': todo['completed']
    })

with open('todo_all_employees.json', 'w') as f:
    json.dump(data, f, indent=4)
