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
    ...

def search_password():
    ...

def generate_password():
    ...


def update_data(website, data):
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

