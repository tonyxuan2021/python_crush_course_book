import json

username = input("what is your name?")
filename = "username.json"

try:
    with open(filename) as f:
        json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"we will remember you when you come back, {username}")
else:
    print(f"Welcome back, {username}!")
