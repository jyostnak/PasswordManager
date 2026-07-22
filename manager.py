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
                update_data(website, data)
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

    # Load the data
    data = storage.load_data()

    # Handle the case if the file is empty
    if not data:
        print("No passwords are stored.")
        return

    # If not empty, print the data
    for website, details in data.items():
        print(f"Website  : {website}")
        print(f"Username : {details['username']}")
        print(f"Password : {details['password']}")
        print()


def search_password():
    # Load the data
    data = storage.load_data()

    # Ask the user for input
    website = input("Website: ")

    # Handle the case if the file in empty
    if not data:
        print("No passwords are stored.")
        return
    
    # check if the input matches any of the data in the file
    if website in data:
        details = data[website]
        print(f"Username : {details['username']}")
        print(f"Password : {details['password']}")
        
    else:
        print(f"The information related to {website} does not exist in the file.")


def generate_password():
    ...

def delete_password():
    ...


def update_data(website, data):       # Updates the already existing password or/and username 
    # Ask the user what do they want to update
    while True:

        choice = input("""
    1. Update password
    2. Update username

    What would you like to do? """)

        # Update password
        if choice == '1':
            password = input("New password: ")

            # Confirm password
            for i in range(4):
                confirm_pass = input("Confirm password: ")
                if confirm_pass == password:
                    break

                if i == 3:
                    print("Could not update the password...")
                    return
                
                else:
                    print("Does not match the password. Please check and enter again.")

            # Rewrite the password
            data[website]["password"] = password
            break

        # Update username
        elif choice == '2':
            username = input("New username: ")

            # Rewrite the username
            data[website]["username"] = username
            break

        else:
            print("Enter a valid input.")

    # Add the data back to JSON file
    storage.save_data(data)
    print("Updated successfully!")

