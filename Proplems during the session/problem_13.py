# Bank account

print("Welcome to Bank Masr")

users = {
    "Omar" : "1234",
}

def Login():
    print("\n-- Login --")
    username = input("Enter Your username: ")
    password = input("Enter Your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Wrong username or password!")
        return None
    
def Register():
    print("\n -- Create New Account --")
    username = input("Enter your username: ")

    if username in users:
        print("This username already exists")
        return None, None
    
    password = input("Write a password: ")
    users[username] = password
    print("Accounted created successfully!")
    return username, password

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit ${amount}. New Balance: ${self.balance}")
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdraw ${amount}. New Balance: ${self.balance}")

while True:
    print("\n -- Main menu --")
    print("1- Login")
    print("2- Create Account")
    print("3- exit")
    
    main_choice = input("Choose: ")
    
    match main_choice:
        case "1":
            logged_user = Login()
            if logged_user:
                ac = BankAccount(logged_user, 0)

                while True:
                    print("\n--- Menu ---")
                    print("1- Deposit money")
                    print("2- Withdraw money")
                    print("3- Show balance")
                    print("4- Exit the system")
    
                    choice = input("Choose: ")
    
                    match choice:
                        case "1":
                            amount = int(input("Enter the amount to deposit: "))
                            ac.deposit(amount)
                        case "2":
                            amount = int(input("Enter the amount to withdraw: "))
                            ac.withdraw(amount)
                        case "3":
                            print(f"Your balance: {ac.balance}")
                        case "4":
                            print("You have logged out")
                            break
        case "2":
            Register()
        case "3":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice")