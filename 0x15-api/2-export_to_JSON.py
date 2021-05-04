#!/usr/bin/python3
""" script to fetch data from an APIs """

import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    filename = "{}.json".format(sys.argv[1])

    for i in users:
        if i.get("id") == int(sys.argv[1]):
            employee_name = i.get("username")

    lt1 = []
    for i in todos:
        if i.get("userId") == int(sys.argv[1]):
            dct1 = {}
            dct1["task"] = i.get("title")
            dct1["completed"] = i.get("completed")
            dct1["username"] = employee_name
            lt1.append(dct1)
    dct2 = {}
    dct2[sys.argv[1]] = lt1
    with open(filename, 'w') as file:
        jsonobject = json.dumps(dct2)
        file.write(jsonobject)
