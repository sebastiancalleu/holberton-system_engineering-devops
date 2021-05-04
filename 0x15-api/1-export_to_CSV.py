#!/usr/bin/python3
""" script to fetch data from an APIs """

import csv
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    for i in users:
        if i.get("id") == int(sys.argv[1]):
            employee_name = i.get("name")

with open('{}.csv'.format(sys.argv[1]), 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for i in todos:
        if i.get("userId") == int(sys.argv[1]):
            writer.writerow([sys.argv[1], employee_name,
                             i.get("completed"), i.get("title")])
