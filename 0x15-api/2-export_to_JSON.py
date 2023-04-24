#!/usr/bin/python3
""" Fetching JSON data from API """

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    todo_user = requests.get("{}/todos".format(user_url))
    todo_user = todo_user.json()
    file1_name = user_id + ".json"
    the_dict = {}

    the_dict[user_id] = []

    for elem in todo_user:
        in_dict = {}
        in_dict["task"] = elem.get("title")
        in_dict["completed"] = elem.get("completed")
        in_dict["username"] = user_name
        the_dict.get(user_id).append(in_dict)

    with open(file1_name, 'w') as f1:
        json.dump(the_dict, f1)
