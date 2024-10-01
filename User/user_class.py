import hashlib
import json
import os


class UserApp:
    def __init__(self):
        self.filename = 'data.txt'

    def run(self):
        while True:
            print('''Please choose the options below: 
            1. Log In
            2. Register
            3. Exit
            ''')
            user_choice = input("Enter the choice (1/2/3)")

            match user_choice:
                case "1":
                    self.login_user()
                case "2":
                    self.register_user()
                case "3":
                    print("Existing...")
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
        username = input("Enter your username: ")
        email = input("Enter you email: ")
        password = input("Enter a password: ")

        try:
            # create a new user
            new_user = User(username, email, password)
            # Save the new user
            UserDataManager.save_user(new_user, self.filename)
            print(f"User {username} registered successfully!")

        except Exception as e:
            print(f"Error during registration: {e}")


"""USER CLASS"""
class User:

    def __init__(self, user_name, email, password = None, salt = None, hashed_password = None):
        self.user_name = user_name  #Username
        self.email = email      #User email
        self.salt = salt if salt else os.urandom(16)    # Generate a new slat if nor provided
        self._password = hashed_password if hashed_password else self.hash_password(password)   # Set the password

    def __repr__(self):
        """Representation of the User Object in String"""
        return (f"User Profile: \n"
                f"Username: {self.user_name}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n")

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name, str) and  len(user_name.strip()) >= 3:
            self._user_name = user_name
        else:
            raise ValueError("Username must be a non-empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        if isinstance(email,str) and "." in email and "@" in email:   # if the email contains '.'and '@' then it is set
            self._email = email
        else:
            raise ValueError("Email must contain '@' and '.'")  # else raise Error

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password,str) and len(password.strip()) > 0 : # if the password is a string and it is non-empty
            self._password = self.hash_password(password)
        else:
            raise ValueError("Password must be a non-empty string") # else raise Error


    def hash_password(self,password):
        """Hashes the password with the user's salt"""
        m = hashlib.sha256()            # Hash the password with SHA256
        salted_password = self.salt + password.encode()     # Concatenate salt and password
        m.update(salted_password)
        return m.hexdigest()

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password."""
        hashed_input_password = hashlib.sha256(self.salt + password.encode()).hexdigest()

        if hashed_input_password == self._password:
            return True
        else:
            return False


# Creating a separate class to save user info on a separate file
class UserDataManager:

    @staticmethod
    def save_user(user, filename):
        user_data = {               # A dictionary of user data
            'Username': user.user_name,
            'Email': user.email,
            'Salt': user.salt.hex(),     # Convert binary salt to hex for storage
            'Password': user.password
        }

        try:
            with open(filename, 'a') as file:   # open file and append the user data
                json.dump(user_data, file)
                file.write('\n')

        except Exception as e:
            print(f"Error saving user: {e}")

    @staticmethod
    def load_users(filename):
        users = []         # create an empty list of users objects
        try:
            with open(filename, 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    salt = bytes.fromhex(user_data['Salt'])     # Convert the hex string back to binary
                    user = User(user_data['Username'], user_data['Email'],None, salt, user_data['Password'])
                    users.append(user)

        except Exception as e:
            print(f"Error loading users: {e}")
        return users
