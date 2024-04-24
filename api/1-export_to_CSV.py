#!/usr/bin/python3
"""
Requesting data from rest api
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter user id")
        sys.exit()

    link = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{0}/users/{1}'
                        .format(link, sys.argv[1])).json()
    userTodo = requests.get('{0}/todos?{1}={2}'
                            .format(link, "userId", sys.argv[1])).json()

    csvFormat = []

    for data in userTodo:
        arr = [f"{data['userId']}", f"{user['username']}",
               f"{data['completed']}", f"{data['title']}"]
        csvFormat.append(arr)

    filename = f"{user['id']}.csv"

    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(csvFormat)
