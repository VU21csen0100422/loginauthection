# login_system.py

import hashlib


USER_DETAILS_FILEPATH = "users.txt"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email, password):
    hashed_password = hash_password(password)
    with open(USER_DETAILS_FILEPATH, "a") as file:
        file.write(f"{email}:{hashed_password}\n")
    print("User registered successfully!")


def login_user(email, password):
    hashed_password = hash_password(password)
    with open(USER_DETAILS_FILEPATH, "r") as file:
        for line in file:
            stored_email, stored_hashed_password = line.strip().split(":")
            if email == stored_email and hashed_password == stored_hashed_password:
                return True
    return False

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register_user(email, password)
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if login_user(email, password):
                print("Login successful! Access granted.")
            else:
                print("Invalid credentials. Access denied.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
