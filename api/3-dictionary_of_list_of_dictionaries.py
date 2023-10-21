import json
import requests

# API endpoints
USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

# Fetch all users
users = requests.get(USERS_URL).json()

# Fetch all todos
todos = requests.get(TODOS_URL).json()

# Group todos by user ID
data = {}
for todo in todos:
    user_id = todo['userId']
    username = next(user['username']
                    for user in users if user['id'] == user_id)

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        'username': username,
        'task': todo['title'],
        'completed': todo['completed']
    })

# Write output JSON file
with open('todo_all_employees.json', 'w') as f:
    json.dump(data, f, indent=4)
