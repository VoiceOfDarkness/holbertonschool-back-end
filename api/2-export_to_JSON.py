#!/usr/bin/python3
"""
This module retrieves task information from an API based on a user ID
anddisplays the employee's name,
the number of tasks completed, and the titles of the completed tasks.
"""

import requests
import sys
import json

TASK_URL = "https://jsonplaceholder.typicode.com/todos"
USER_URL = "https://jsonplaceholder.typicode.com/users/"


def employee_info(user_id: str):
    """
    Retrieves task information from an API based
    on a user ID and returns a formatted string
    containing the employee's name, the number of tasks completed, and the
    titles of the completed tasks.

    Args:
        user_id (str): The ID of the user.

    Returns:
        str: A formatted string containing the
        employee's name, the number of tasks completed,
        and the titles of the completed tasks.
    """
    task_response = requests.get(TASK_URL + "?userId=" + user_id).json()
    user_response = requests.get(USER_URL + user_id).json()

    name = user_response.get("username")

    tasks = []
    for task in task_response:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name
        }
        tasks.append(task_info)

    data = {user_id: tasks}

    file_name = f"{user_id}.json"
    with open(file_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: 1-export_to_CSV.py <employee_id>")
    user_id = sys.argv[1]
    employee_info(user_id)
