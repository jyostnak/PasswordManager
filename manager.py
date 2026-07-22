import storage

def add_password():        # Adds password and it's related details into the JSON file

    # Take the input from user
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    # Load the data
    data = storage.load_data()

    # Update the data
    data[website] = {
        "username" : username,
        "password" : password
    }

    # Add the data back to the file
    storage.save_data(data)
    



def view_passwords():
    ...

def search_password():
    ...

def generate_password():
    ...