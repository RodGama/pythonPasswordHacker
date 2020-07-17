import json


# write your code here
with open("users.json", "r") as json_file:
    users = json.load(json_file)
print(len(users["users"]))
