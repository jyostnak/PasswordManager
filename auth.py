import manager
import storage

def master_exists():     # Checks if the master password exists or not

    # Load the data from the JSON file
    data = storage.load_data("master.json")

    # Check if it is empty or not
    if not data:
        return False

    else:
        return True


def create_master_password():     # Creates the master password for the new users

    data = {}

    while True:

        # Ask the iser if they want to create their own password or want us to generate it
        choice = input("Do you want us to generate the password:(y/n) ")

        # Generate password
        if choice == 'y':
            password = manager.generate_password()
            print(f"Password: {password}")

        elif choice == 'n':

            password = input("Password: ")

            # Confirm password
            for i in range(4):

                confirm_pass = input("Confirm password: ")

                if confirm_pass == password:
                    break

                if i == 3:
                    print("Error: Too many wrong entries.")
                    return
                
                else:
                    print("Does not match the password. Please check and enter again.")
            break

        else:
            print("Enter a valid input.")

        data['password'] = password

    storage.save_data(data)


def verify_master_password():     # Check if the master password extered by the user matches the actual password or not

    # Load the data
    data = storage.load_data("master.json")

    # Ask the user for input
    password = input("Password: ")

    # Check if the password matches or not
    if data['password'] == password:
        return True
    
    else:
        return False
    

def change_master_password():     # Allows the user to change the master password if they want to

    data = storage.load_data("master.json")

    for i in range(3):

        confirm = input("Enter the previous password: ")

        if confirm == data['password']:

            password = input("Password: ")

            # Confirm password
            for i in range(4):

                confirm_pass = input("Confirm password: ")

                if confirm_pass == password:
                    data['password'] = password
                    break

                if i == 3:
                    print("Error: Too many wrong entries.")
                    return
                
                else:
                    print("Does not match the password. Please check and enter again.")

                break

            if i == 2:
                print("Access denied.")
                return 

            else:
                print("Incorrect. Try again.")   

    storage.save_data(data, "master.json")     

