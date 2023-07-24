#!/usr/bin/python3
"""
This script uses the JSON placeholder REST API,
to fetch information for a given employee ID,
returns information about his/her TODO list progress.

Usage: ./1-export_to_CSV.py <employee_id>

The script accepts an integer as a parameter, which is the employee ID
The script exports data of the employee's todo  in the CSV format:
    -"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    -Saves them in a file USER_ID.csv
"""
import requests
import sys
import csv


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
            for task in tasks:
                if task.get("userId") == user.get("id"):
                    data.append([
                        task.get("userId"),
                        user.get("username"),
                        task.get("title"),
                        str(task.get("completed"))
                    ])
            if data:
                with open('{}.csv'.format(q), 'w', encoding='UTF8') as f:
                    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                    writer.writerows(data)
