#!/usr/bin/python3
"""
This is a script that accepts user id and displays the tasks from an api
https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("User id not specified")
        exit(1)
    params = {'id': argv[1]}
    url = 'https://jsonplaceholder.typicode.com/'
    with requests.get(url + 'users', params=params) as emp_response:
        users = emp_response.json()
        if users:
            employee = users[0]
            params = {"userId": employee['id']}
            with requests.get(url + 'todos', params=params) as todo_res:
                todos = todo_res.json()
                completed = [task for task in todos if task['completed']]
                print(
                    "Employee {:s} is done with tasks({}/{}):".format(
                        employee['name'],
                        len(completed),
                        len(todos)
                    ))
                for task in completed:
                    print("\t  {}".format(task['title']))
                exit(0)
        else:
            print("User with id {} not found".format(argv[1]))
    exit(1)
