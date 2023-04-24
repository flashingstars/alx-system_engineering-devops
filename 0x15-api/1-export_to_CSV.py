#!/usr/bin/python3
""" Fetching JSON data from API """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    todo_user = requests.get("{}/todos".format(user_url))
    todo_user = todo_user.json()
    file1_name = user_id + ".csv"

    with open(file1_name, 'w') as csvfile:
        for item in todo_user:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), user_name, item.get("completed"),
                item.get("title")))
