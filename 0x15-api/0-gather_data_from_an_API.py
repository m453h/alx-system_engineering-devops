#!/usr/bin/python3
"""
This script uses the JSON placeholder REST API,
to fetch information for a given employee ID,
returns information about his/her TODO list progress.

Usage: ./0-gather_data_from_an_API.py <employee_id>

The script accepts an integer as a parameter, which is the employee ID
The script displays on the standard output the employee
TODO list progress in this exact format:
    -First line: Employee EMPLOYEE_NAME is done with tasks
                 (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
                  - EMPLOYEE_NAME: name of the employee
                  - NUMBER_OF_DONE_TASKS: number of completed tasks
                  - TOTAL_NUMBER_OF_TASKS: total number of tasks,
                                           which is the sum of
                                           completed and non-completed
                                           tasks
    -Second and N next lines display the title of completed tasks:
                TASK_TITLE (with 1 tabulation and 1
                            space before the TASK_TITLE)

"""
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
            employee_task = []
            completed_tasks = 0
            total_tasks = 0
            for task in tasks:
                if task.get("userId") == user.get("id"):
                    total_tasks += 1
                    if task.get("completed"):
                        completed_tasks += 1
                        employee_task.append(task.get("title"))

            print("Employee {} is done with tasks({}/{}):".format(
                user.get("name"), completed_tasks, total_tasks)
                )
            for task in employee_task:
                print("\t {}".format(task))
