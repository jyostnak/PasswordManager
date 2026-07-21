# The main menu

print("\nPASSWORD MANAGER")

while True:                                 # Loop runs until the user enters a valid input or the user wants to exit
    
    print("""
          1. Add password
          2. View password
          3. Search password
          4. Exit
          """)
    choice = input("\nWhat would you like to do? ").strip()
    
    if choice == '1':                       # Adds the password to json file
        
        while True:                         # Loop runs until the user enters a valid input
            
            print("\n1. Generate password\n2. Create your own password")
            order = input("\nWhat would you like to do? ").strip()
            
            if order == '1':  # Generates a password
                print("Generate")
                break
            
            elif order == '2':              # Allows you to create your own password
                print("Create your own")
                break
            
            else:
                print("\nEnter a valid input.")
    
    elif choice == '2':                     # The user can view previously saved passwords in the json file
        print("View")
    
    elif choice == '3':
        print("Searching...")               # The user can search the required website's password along with the username
    
    elif choice == '4':                     # User exits the main menu
        break
    
    else:
        print("Enter a valid input.")
    
        