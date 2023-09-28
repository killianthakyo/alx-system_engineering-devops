#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    csv_file_name = f"{sys.argv[1]}.json"
    user_id = user.get("id")
    username = user.get("username")

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for t in todos:
            csv_writer.writerow(
                    [user_id, username, t.get("completed"), t.get("title")])
