#!/usr/bin/python3
"""
This script uses the JSON placeholder REST API,
to fetch information for all employees it
returns information about their TODO list progress.

Usage: ./3-dictionary_of_list_of_dictionaries.py

The script accepts an integer as a parameter, which is the employee ID
The script exports data of the employee's todo  in the JSON format:
    {"USER_ID":
    [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}"
    -Saves them in a file todo_all_employees.json
"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(url)).json()
    tasks = requests.get("{}/{}".format(url, "todos")).json()
    json_data = {}
    for user in users:
        data = []
        for task in tasks:
            if task.get("userId") == user.get("id"):
                data.append({
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username"),
                })
        if data:
            json_data[user.get("id")] = data

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(json_data, f)
