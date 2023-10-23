#!/usr/bin/python3
"""
This is a script that accepts user id and writes the tasks to a csv file
https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("User id not specified")
        exit(1)
    userId = argv[1]
    params = {'id': userId}
    url = 'https://jsonplaceholder.typicode.com/'
    with requests.get(url + 'users', params=params) as emp_response:
        users = emp_response.json()
        if users:
            employee = users[0]
            params = {"userId": employee['id']}
            with requests.get(url + 'todos', params=params) as todo_res:
                todos = todo_res.json()
                with open(userId + '.csv', "w") as csv:
                    lines = []
                    for task in todos:
                        lines.append(
                            '"{}","{}","{}","{}"\n'.format(
                                userId,
                                employee['username'],
                                task['completed'],
                                task['title']
                            )
                        )
                    csv.writelines(lines)
        else:
            print("User with id {} not found".format(userId))
