# bankSystem
this is just my college project
# Bank System Python Project

## Overview
This Python project implements a simple banking system with user registration, login, deposit, and withdrawal functionalities. User data is stored in a JSON file, allowing for persistent storage of user information and balances.

## Project Structure
- **bank_system.py:** Main Python script containing the BankSystem class.
- **users.json:** JSON file storing user information.

## Usage
1. Run the script `bank_system.py` to start the program.
2. The program will display a menu with options for user registration, login, and exit.
3. If choosing user registration, provide required information such as first name, last name, national code, username, and password.
4. If choosing user login, enter the username and password.
5. After successful login, the main menu is displayed with options to deposit, withdraw, or exit.
6. Deposit and withdrawal operations update the user's balance in the `users.json` file.

## Dependencies
- Python 3.x

## Project Files
- **bank_system.py**
```python
# (Include the content of your Python script here)
```

- **users.json**
```json
[
  // Example user data will be stored here after registration and transactions
]
```

## Notes
- Ensure that the `users.json` file is present and has the correct format.
- This project is a basic demonstration and does not include advanced security measures or error handling.

Feel free to explore and modify the script to meet your specific requirements or extend its functionality. If you have any questions or encounter issues, please refer to the script or contact the project author.
