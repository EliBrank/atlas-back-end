#!/usr/bin/python3

"""defines get_todo_progress function"""

import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_todo_progress():
    """gets todo info for specified employee

    args:
        employee_id: used to specify employee
    """

    url_employees = f"{BASE_URL}/users"
    response_employees = requests.get(url_employees)

    url_all_todos = f"{BASE_URL}/todos"
    response_all_todos = requests.get(url_all_todos)

    if (
        response_employees.status_code == 200
        and response_all_todos.status_code == 200
    ):
        employee_data = response_employees.json()
        todo_data = response_all_todos.json()

        json_todo_data_dict = {}
        for employee in employee_data:
            json_todo_data = []
            employee_id = employee.get("id")
            for task in todo_data:
                if employee_id == task.get("userId"):
                    json_todo_data.append({
                        "username": employee.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    })
            json_todo_data_dict.update({employee_id: json_todo_data})

        with open("todo_all_employees.json", mode="w") as jsonfile:
            json.dump(json_todo_data_dict, jsonfile)


if __name__ == "__main__":
    get_todo_progress()
