import json
import re   # Import regex for email validation
import hashlib
import os


class UserApp:
    def __init__(self):
        self.filename = 'data.txt'

    def run(self):
        while True:
            print('''Please choose the options below: 
            1. Log In
            2. Register
            3. Reset Password
            4. Exit
            ''')
            user_choice = input("Enter the choice (1/2/3/4)")

            match user_choice:
                case "1":
                    self.login_user()
                case "2":
                    self.register_user()
                case "3":
                    self.reset_password()
                case "4":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice. Please try again")

    def login_user(self):
        """Login process for existing users"""
        username = input("Enter your Username:")
        password = input("Enter password: ")

        try:
            # Load existing users from the file
            users = UserDataManager.load_users(self.filename)

            # Check if the username exists
            for user in users:
                if user.user_name == username:
                    if user.check_password(password):
                        print("Login successful!")
                        return
                    else:
                        print("Incorrect password.")
                        return
            print("Username not found.")

        except Exception as e:
            print(f"Error during login: {e}")

    def register_user(self):
        """registration process for new users"""
        username = input("Enter your username: ").strip()
        email = input("Enter you email: ").strip()


        password = input("Enter a password: ")
        password_confirm = input("Confirm your password: ").strip()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Error: Invalid email format.")
            return

        # Validate password strength
        if not self.is_strong_password(password):
            print("Password must be at least 8 characters long and contain a mix of letters, numbers, and special "
                  "characters.")
            return

        # Check if the username or email already exists
        if self.is_user_exists(username, email):
            print("Username or email already exists.")
            return

        if password != password_confirm:
            print("Passwords do not match.")
            return

        try:
            # create a new user
            new_user = User(username, email, password)
            # Save the new user
            UserDataManager.save_user(new_user, self.filename)
            print(f"User {username} registered successfully!")

        except Exception as e:
            print(f"Error during registration: {e}")

    def is_user_exists(self, username, email):
        """Check if the username or email already exists in the user data."""
        users = UserDataManager.load_users(self.filename)
        for user in users:
            if user.user_name == username or user.email == email:
                return True
        return False

    def is_strong_password(self,password):
        """Check if the password is strong enough."""
        return len(password) >= 8 and any(c.isdigit() for c in password) \
            and any(c.isalpha() for c in password) and any(not c.isalnum() for c in password)

    def reset_password(self):
        """Reset user password process."""
        email = input("Enter your email: ").strip()

        # Load users to find the user by email
        users = UserDataManager.load_users(self.filename)
        user = next((user for user in users if user.email == email), None)

        if user:
            new_password = input("Enter your new password: ").strip()
            if self.is_strong_password(new_password):
                user.password = new_password    # Automatically hashes the new password
                UserDataManager.save_user(user, self.filename)  # Save updated user
                print("Password reset successfully!")
            else:
                print("Password does not meet strength requirements.")
        else:
            print("No user found with that email.")


"""USER CLASS"""
class User:
    def __init__(self, user_name, email, password=None, salt=None, hashed_password=None):
        self.user_name = user_name
        self.email = email
        self.salt = salt if salt else os.urandom(16)
        self._password = hashed_password if hashed_password else self.hash_password(password)

    def __repr__(self):
        """Representation of the User Object in String."""
        return (f"User Profile: \n"
                f"Username: {self.user_name}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n")

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name, str) and len(user_name.strip()) >= 3:
            self._user_name = user_name
        else:
            raise ValueError("Username must be a non-empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and "." in email and "@" in email:
            self._email = email
        else:
            raise ValueError("Email must contain '@' and '.'")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password.strip()) > 0:
            self._password = self.hash_password(password)
        else:
            raise ValueError("Password must be a non-empty string")

    def hash_password(self, password):
        """Hashes the password with the user's salt."""
        m = hashlib.sha256()
        salted_password = self.salt + password.encode()
        m.update(salted_password)
        return m.hexdigest()

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password."""
        hashed_input_password = hashlib.sha256(self.salt + password.encode()).hexdigest()
        return hashed_input_password == self._password

class UserDataManager:
    @staticmethod
    def save_user(user, filename):
        user_data = {
            'Username': user.user_name,
            'Email': user.email,
            'Salt': user.salt.hex(),
            'Password': user.password
        }

        try:
            with open(filename, 'a') as file:
                json.dump(user_data, file)
                file.write('\n')
        except Exception as e:
            print(f"Error saving user: {e}")

    @staticmethod
    def load_users(filename):
        users = []  # Create an empty list of user objects
        try:
            with open(filename, 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    salt = bytes.fromhex(user_data['Salt'])  # Convert the hex string back to binary
                    user = User(user_data['Username'], user_data['Email'], None, salt, user_data['Password'])
                    users.append(user)
        except Exception as e:
            print(f"Error loading users: {e}")
        return users
