#!/usr/bin/python3

"""defines get_todo_progress function"""

import json
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

        json_todo_data = []
        for task in todo_data:
            json_todo_data.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_data.get("username"),
            })

        json_todo_data_dict = {f"{employee_id}": json_todo_data}

        with open(f"{employee_id}.json", mode="w") as jsonfile:
            json.dump(json_todo_data_dict, jsonfile)


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
