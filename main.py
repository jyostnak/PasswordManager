# The main menu

print("\nPASSWORD MANAGER")

while True:                                 
# Loop runs until the user enters a valid input or the user wants to exit
    
    print("""
          1. Add password
          2. View password
          3. Search password
          4. Exit
          """)
    choice = input("\nWhat would you like to do? ").strip()
    
    # Adds the password to json file
    if choice == '1':                       
        
        while True:                         
        # Loop runs until the user enters a valid input
            
            print("\n1. Generate password\n2. Create your own password")
            order = input("\nWhat would you like to do? ").strip()
            
            # Generates a password
            if order == '1':  
                print("Generate")
                break
            
            # Allows you to create your own password
            elif order == '2':              
                print("Create your own")
                break
            
            else:
                print("\nEnter a valid input.")
    
    # The user can view previously saved passwords in the json file
    elif choice == '2':                     
        print("View")
    
    # The user can search the required website's password along with the username
    elif choice == '3':
        print("Searching...")               
    
    # User exits the main menu
    elif choice == '4':                     
        break
    
    # Warn the user, if entered a wrong input
    else:
        print("Enter a valid input.")
    
        