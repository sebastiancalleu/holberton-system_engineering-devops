#!/usr/bin/python3
""" script to fetch data from an APIs """

import requests
import sys

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
users = requests.get("https://jsonplaceholder.typicode.com/users").json()

number_of_done_tasks = 0
total_number_of_tasks = 0
tasks = ""
for i in todos:
    if i.get("userId") == int(sys.argv[1]):
        total_number_of_tasks += 1
        if i.get("completed") == True:
            number_of_done_tasks += 1
            tasks += "\t " + i.get("title") + "\n"

for i in users:
    if i.get("id") == int(sys.argv[1]):
        employee_name = i.get("name")

print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_done_tasks, total_number_of_tasks))
print(tasks, end="")
