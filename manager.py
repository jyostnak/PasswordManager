import storage

def add_entry():        # Adds password and it's related details into the JSON file

    # Load the data
    data = storage.load_data()

    # Take the input from user
    website = input("Website: ")

    # Check if the website already exists in the file
    if website in data:
        # Ask the user if they want to rewtire the existing password or username

        print("This website data already exists.")

        while True:
            # Loop runs until user enters a valid input

            choice = input("Would you like to update it?(y/n) ")

            # Update data
            if choice == 'y':
                update_data(website)
                return

            elif choice == 'n':
                return

            else:
                print("Enter a valid input.")
        
    else:
        username = input("Username: ")
        password = input("Password: ")

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

def update_data(website):
    # Ask the user what do they want to update
    ...

    # Update password
    ...

    # Update username
    ...

    # Rewrite the updated info into the JSON file
    ...