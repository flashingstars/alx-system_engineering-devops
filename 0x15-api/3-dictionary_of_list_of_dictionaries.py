#!/usr/bin/python3
""" Fetching JSON data from  API and displaying all """

import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    user_dict = requests.get(user_url).json()
    file1_name = "todo_all_employees.json"
    the_dict = {}

    for elem in user_dict:
        name = elem.get("username")
        user_id = str(elem.get("id"))
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()
        the_dict[user_id] = []
        for item in user_data:
            in_dict = {}
            in_dict["username"] = name
            in_dict["task"] = item.get("title")
            in_dict["completed"] = item.get("completed")
            the_dict[user_id].append(in_dict)

    with open(file1_name, 'w') as f:
        json.dump(the_dict, f)
