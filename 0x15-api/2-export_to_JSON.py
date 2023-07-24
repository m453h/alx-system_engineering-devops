#!/usr/bin/python3
"""
This script uses the JSON placeholder REST API,
to fetch information for a given employee ID,
returns information about his/her TODO list progress.

Usage: ./2-export_to_JSON.py <employee_id>

The script accepts an integer as a parameter, which is the employee ID
The script exports data of the employee's todo  in the JSON format:
    {"USER_ID":
    [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}"
    -Saves them in a file USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        try:
            q = int(sys.argv[1])
        except ValueError:
            q = None

    url = "https://jsonplaceholder.typicode.com"

    if isinstance(q, int):
        user = requests.get("{}/users/{}".format(url, q)).json()
        if user:
            tasks = requests.get("{}/{}".format(url, "todos")).json()
            data = []
            json_data = {}
            for task in tasks:
                if task.get("userId") == user.get("id"):
                    data.append({
                        "task": task.get("title"),
                        "completed": str(task.get("completed")),
                        "username": user.get("username")
                    })
            if data:
                json_data = {user.get("id"): data}
                with open('{}.json'.format(q), 'w', encoding='UTF8') as f:
                    json.dump(json_data, f)
