import auth
import manager
import storage


def main():
    print("\nPASSWORD MANAGER")

    while True:                                 
    # Loop runs until the user enters a valid input or the user wants to exit
        
        print("""
1. Add password
2. View password
3. Search password
4. Delete password
5. Change master password
6. Exit
""")
        choice = input("What would you like to do? ").strip()
        
        # Adds password and it's related details into the JSON file
        if choice == '1':                       
            manager.add_entry()
        
        # The user can view previously saved passwords in the json file
        elif choice == '2':                     
            manager.view_passwords()
        
        # Searches for the required website details
        elif choice == '3':
            manager.search_password()              
        
        # Deletes the data that the user doesn't require
        elif choice == '4':                     
            manager.delete_password()

        # User exits the main menu
        elif choice == '5':
            auth.change_master_password()

        elif choice == '6':
            break
        
        # Warn the user, if entered a wrong input
        else:
            print("Enter a valid input.")

if auth.master_exists():
    for attempt in range(3):
        if auth.verify_master_password():
            main()
            break
        else:
            if attempt == 2:
                print("Incorrect password.\nAccess denied")

            else:
                print("Incorrect password. Check and try again.")

else:
    auth.create_master_password()
    
    for attempt in range(3):
        if auth.verify_master_password():
            main()
            break
        else:
            if attempt == 2:
                print("Incorrect password.\nAccess denied")

            else:
                print("Incorrect password. Check and try again.")


if __name__ == "__main__":
    storage.create_storage_file("master.json")
    storage.create_storage_file("passwords.json")
