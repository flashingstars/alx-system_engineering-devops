#!/usr/bin/python3
""" Fetchong JSON data from API """

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1].strip()
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("name")
    user_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todo = user_todo.json()
    all_todo = 0
    complete_titles = []
    all_completed = 0

    for item in user_todo:
        if item.get("userId") == int(user_id):
            all_todo += 1
            if item.get("completed") is True:
                all_completed += 1
                complete_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, all_completed, all_todo))
    for title in complete_titles:
        print("\t {}".format(title))
