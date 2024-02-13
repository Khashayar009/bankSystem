import json

class BankSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.login_user_code = None

    def display_first_menu(self):
        print("1. User Registration")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice

    def register_user(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        national_code = input("Enter National Code: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'national_code': national_code,
            'username': username,
            'password': password,
            'balance': 0
        }

        with open(self.users_file, 'a') as file:
            file.write(json.dumps(new_user) + '\n')

        print("User registered successfully!")

    def login_user(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        with open(self.users_file, 'r') as file:
            for line in file:
                user_data = json.loads(line)
                if user_data['username'] == username and user_data['password'] == password:
                    self.login_user_code = user_data['national_code']
                    print("Login successful!")
                    return True

        print("Invalid username or password. Please try again.")
        return False

    def display_main_menu(self):
        print("\nMain Menu:")
        print("1. Deposit to Account")
        print("2. Withdraw from Account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice

    def deposit_to_account(self):
        amount = float(input("Enter the deposit amount: "))
        with open(self.users_file, 'r') as file:
            users_data = [json.loads(line) for line in file]

        for user in users_data:
            if user['national_code'] == self.login_user_code:
                user['balance'] += amount
                break

        with open(self.users_file, 'w') as file:
            for user in users_data:
                file.write(json.dumps(user) + '\n')

        print("Deposit successful!")

    def withdraw_from_account(self):
        amount = float(input("Enter the withdrawal amount: "))
        with open(self.users_file, 'r') as file:
            users_data = [json.loads(line) for line in file]

        for user in users_data:
            if user['national_code'] == self.login_user_code:
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    break
                else:
                    print("Insufficient funds. Withdrawal failed.")
                    return

        with open(self.users_file, 'w') as file:
            for user in users_data:
                file.write(json.dumps(user) + '\n')

        print("Withdrawal successful!")

    def run(self):
        while True:
            choice = self.display_first_menu()

            if choice == '1':
                self.register_user()
            elif choice == '2':
                if self.login_user():
                    while True:
                        main_menu_choice = self.display_main_menu()
                        if main_menu_choice == '1':
                            self.deposit_to_account()
                        elif main_menu_choice == '2':
                            self.withdraw_from_account()
                        elif main_menu_choice == '3':
                            self.login_user_code = None
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == '3':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()