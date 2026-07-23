# The main menu

print("\nPASSWORD MANAGER")

while True:                                 
# Loop runs until the user enters a valid input or the user wants to exit
    
    print("""
          1. Add password
          2. View password
          3. Search password
          4. Delete password
          5. Exit
          """)
    choice = input("\nWhat would you like to do? ").strip()
    
    # Adds password and it's related details into the JSON file
    if choice == '1':                       
        ...
    
    # The user can view previously saved passwords in the json file
    elif choice == '2':                     
        print("View")
    
    # Searches for the required website details
    elif choice == '3':
        print("Searching...")               
    
    # Deletes the data that the user doesn't require
    elif choice == '4':                     
        ...

    # User exits the main menu
    elif choice == '5':
        break
    
    # Warn the user, if entered a wrong input
    else:
        print("Enter a valid input.")
    
        