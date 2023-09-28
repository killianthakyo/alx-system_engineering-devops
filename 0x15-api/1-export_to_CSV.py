#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import csv
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    csv_file_name = f"{sys.argv[1]}.json"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(todos)
    #completed = [t.get("title") for t in todos if t.get("completed") is True]
    #print("Employee {} is done with tasks({}/{}):".format(
    #   user.get("name"), len(completed), len(todos)))
    #[print("\t {}".format(c)) for c in completed]
