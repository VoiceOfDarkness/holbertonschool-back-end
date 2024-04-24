#!/usr/bin/python3
"""
This module retrieves task information from an API based on a user ID
anddisplays the employee's name,
the number of tasks completed, and the titles of the completed tasks.
"""

import csv
import requests
import sys

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

    with open(f"{user_id}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in task_response:
            writer.writerow([user_id, name, task.get("completed"),
                             task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: 1-export_to_CSV.py <employee_id>")
    user_id = sys.argv[1]
    employee_info(user_id)
