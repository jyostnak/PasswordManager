import json

def create_storage_file():                                                      
    # Creates a JSON file in case it doesn't exist

    try:
        with open("passwords.json", "x") as file:
            json.dump({}, file)
        
    except PermissionError:    
        # In case the user doesn't have access to the file                                          
        print("You do not have the permission to access this file.")
    
    except FileExistsError:     
        # Does not crash if the file already exists                                         
        pass
    
    except OSError as e:    
        # Operating System error                                            
        print(f"An operating system error occured: {e}")
        
    
def load_data():                                                        
    # Reads the data present in the JSON file

    try:
        data = {}
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("The file does not exist.")

    except PermissionError:
        print("You do not have the permission to access this file.")

    except json.JSONDecodeError:                                                                      
        # In case someone edited the data manually in wrong format
        print("The file contents are not in the JSON format. Kindly check the file and try again.")

    except OSError as e:
        print(f"An operating system error occured: {e}")

    return data


def save_data(data):                                                  
    # Writes the data into the JSON file
    
    try:
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)

    except TypeError:                                                             
        # In case the data entered by the user cannot be added into the JSON file
        print("Kindly enter valid data that can be added into the file.")

    except OSError as e:
        print(f"An operating system error has occured: {e}")

    except PermissionError:
        print("You do not have the permission to access this file.")
