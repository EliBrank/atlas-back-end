#!/usr/bin/python3

"""defines get_todo_progress function"""

import csv
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_todo_progress(employee_id: str):
    """gets todo info for specified employee

    args:
        employee_id: used to specify employee
    """

    url_employee = f"{BASE_URL}/users/{employee_id}"
    response_employee = requests.get(url_employee)

    url_todos = f"{BASE_URL}/users/{employee_id}/todos"
    response_todos = requests.get(url_todos)

    if (
        response_employee.status_code == 200
        and response_todos.status_code == 200
    ):
        employee_data = response_employee.json()
        todo_data = response_todos.json()

        csv_data = []
        for task in todo_data:
            csv_data.append({
                "USER_ID": employee_data.get("id"),
                "USERNAME": employee_data.get("username"),
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

        with open(f"{employee_id}.csv", mode="w") as csvfile:
            # fieldnames pulled from csv_data dict dynamically
            fieldnames = csv_data[0].keys()
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL
            )
            # writer.writeheader()
            # writerows iterates through csv_data list
            writer.writerows(csv_data)


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        employee_id = None
        try:
            int(argv[1])
            employee_id = argv[1]
        except ValueError:
            print("employee id must be an integer")

        if employee_id:
            get_todo_progress(employee_id)
