#!/usr/bin/python3
"""
This is a script that accepts user id and writes the tasks to a json file
https://jsonplaceholder.typicode.com/
"""
import json
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
                with open(userId + '.json', "w") as json_file:
                    for task in todos:
                        del task['userId']
                        del task['id']
                        task['task'] = task.pop('title')
                        task['username'] = employee['username']
                    entry = {userId: todos}
                    json_file.write(json.dumps(entry))
        else:
            print("User with id '{}' not found".format(userId))
