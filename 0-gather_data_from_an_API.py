#!/usr/bin/python3
import requests

import sys

TASK_URL = 'https://jsonplaceholder.typicode.com/todos'
USER_URL = 'https://jsonplaceholder.typicode.com/users/'


def employee_info(user_id: str):
    task_response = requests.get(TASK_URL + "?userId=" + user_id).json()
    user_response = requests.get(USER_URL + user_id).json()

    name = user_response.get('name')
    total_tasks = len(task_response)
    done_tasks = len([task for task in task_response if task.get('completed') is True])
    title_tasks = [task.get('title') for task in task_response if task.get('completed') is True]
    
    result = f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):\n\t "
    result += "\n\t ".join(title_tasks)

    return result


if __name__ == "__main__":
    user_id = sys.argv[1]
    print(employee_info(user_id))