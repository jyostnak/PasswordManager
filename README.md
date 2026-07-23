# 🔐 Password Manager

A simple command-line Password Manager built with Python that allows users to securely store and manage their login credentials using a master password.

## Features

- Create and verify a master password
- Secure master password storage using SHA-256 hashing
- Generate strong random passwords
- Add new website credentials
- Search for saved passwords
- View all stored passwords
- Update existing usernames and passwords
- Delete saved passwords
- Store data persistently using JSON files
- Handle common file and input errors gracefully

## Project Structure

```
PasswordManager/
│── main.py          # Entry point of the application
│── manager.py       # Password management functions
│── auth.py          # Master password authentication
│── storage.py       # JSON file handling
│── passwords.json   # Stores website credentials
│── master.json      # Stores the hashed master password
```

## Requirements

- Python 3.10 or above

This project uses only Python's standard library and does not require any external packages.

## Modules Used

- `json`
- `hashlib`
- `secrets`
- `string`

## How It Works

### First Launch

- The application creates `master.json` and `passwords.json` if they do not already exist.
- The user creates a master password.
- The master password is hashed using SHA-256 before being stored.

### Subsequent Launches

- The user enters the master password to unlock the application.
- If the password is correct, access to the password manager is granted.
- Up to three authentication attempts are allowed.

## Menu

```
1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Change Master Password
6. Exit
```

## Password Generator

The built-in password generator:

- Generates passwords between **8 and 16 characters**
- Includes at least:
  - One uppercase letter
  - One lowercase letter
  - One digit
  - One special character
- Uses Python's `secrets` module to generate cryptographically secure passwords.

## Security

- Master passwords are stored as SHA-256 hashes.
- Website names are normalized to enable case-insensitive searching.
- Password generation uses Python's `secrets` module for improved security.

> **Note:** Website passwords are currently stored in plain text in `passwords.json`. Encrypting stored passwords is planned for a future version.

## Future Improvements

- Encrypt stored passwords
- Hide password input using the `getpass` module
- Password strength checker
- Export and import passwords
- Copy passwords to the clipboard
- GUI version using Tkinter or PyQt

## Author

Developed by **Jyostna K**.
