import json

filename = "usernames.json"


with open(filename) as f:
    usernames = json.load(f)
    print(f"Welcome back {usernames}")
    


