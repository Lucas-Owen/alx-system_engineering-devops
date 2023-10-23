#!/usr/bin/python3
"""
This is a script that accepts user id and writes the tasks to a json file
https://jsonplaceholder.typicode.com/
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    with requests.get(url + 'users') as emp_response:
        users = emp_response.json()
        if users:
            entries = dict()
            with open('todo_all_employees.json', "w") as json_file:
                for employee in users:
                    userId = employee['id']
                    params = {"userId": userId}
                    with requests.get(url + 'todos', params=params) as todo_r:
                        todos = todo_r.json()
                        for task in todos:
                            del task['userId']
                            del task['id']
                            task['username'] = employee['username']
                        entries[userId] = todos
                json_file.write(json.dumps(entries))
