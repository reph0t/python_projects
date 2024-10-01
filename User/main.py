from user_class import User, UserDataManager

class UserApp:
    def run(self):
        while True:
            try:
                user_name_input = input("Enter Username (or 'exit' to quit): ")
                if user_name_input.lower() == 'exit':
                    print("Exiting program...")
                    break
                email_input = input("Enter E-mail: ")
                pass_input = input("Enter Password: ")

                user = User(user_name_input, email_input, pass_input)

                UserDataManager.save_user(user, "data.txt")
                print(f"Information has been added to file.")

            # Catch validation errors from the setters
            except ValueError as e:
                print(f"Error: {e}")

            # Optional general exception handler for any other unforeseen issues
            except Exception as e:
                print(f"Error occurred: {e}")

if __name__ == "__main__":
    app = UserApp()
    app.run()





