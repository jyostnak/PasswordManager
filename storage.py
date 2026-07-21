import json

def load_data():                                                      # Creates a JSON file in case it doesn't exist
    with open("passwords.json", "w") as file:
        json.dump({}, file)


try:
    with open("passwords.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:                                            # If the file does not exists, load_data function is called
    load_data()
except PermissionError:                                              # In case the user doesn't have access to the file
    print("You do not have the permission to access this file")

