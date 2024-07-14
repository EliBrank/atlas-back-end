#!/usr/bin/python3

"""defines get_todo_progress function"""

import requests
from sys import argv

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

        employee_name = employee_data.get("name")

        employee_tasks = []
        completed_tasks = []

        for task in todo_data:
            # task titles are extracted from obj and put into list
            employee_tasks.append(task.get("title"))
            if task.get("completed"):
                completed_tasks.append(task.get("title"))

        print(f"Employee {employee_name} is done with tasks"
              f"({len(completed_tasks)}/{len(employee_tasks)}):")
        for task in completed_tasks:
            print(f"\t {task}")


if __name__ == "__main__":

    if len(argv) == 2:
        employee_id = None
        try:
            int(argv[1])
            employee_id = argv[1]
        except ValueError:
            print("employee id must be an integer")

        if employee_id:
            get_todo_progress(employee_id)
