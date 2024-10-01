import hashlib
import json
import os


class User:

    def __init__(self,user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.salt = os.urandom(16)      # Generate a new salt
        self.password = self.hash_password(password)    # Hash the password with salt

    def __repr__(self):
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
        if isinstance(email,str) and "." in email and "@" in email:
            self._email = email
        else:
            raise ValueError("Email must contain '@' and '.'")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password,str) and len(password.strip()) > 0 :
            self._password = self.hash_password(password)
        else:
            raise ValueError("Password must be at least 6 characters long.")


    def hash_password(self,password):
        """Hashes the password with the user's salt"""
        m = hashlib.sha256()
        salted_password = self.salt + password.encode()     # Concatenate salt and password
        m.update(salted_password)
        return m.hexdigest()

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password."""
        hashed_input_password = hashlib.sha256(self.salt + password.encode()).hexdigest()

        if hashed_input_password == self._password:
            print("Password matches")
            return True
        else:
            raise ValueError("Password does not match")
            return False

# Creating a separate class to save user info on a separate file
class UserDataManager:

    @staticmethod
    def save_user(user, filename):
        user_data = {
            'Username': user.user_name,
            'Email': user.email,
            'Salt': user.salt.hex(),     # Convert binary salt to hex for storage
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
        users = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    salt = bytes.fromhex(user_data['Salt'])
                    user = User(user_data['Username'], user_data['Email'], user_data['Hashed Password'])
                    user.salt = salt
                    users.append(user)

        except Exception as e:
            print(f"Error loading users: {e}")
        return users
