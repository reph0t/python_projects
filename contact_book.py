import json
contact_book={}

print("Contact Book version 1.0\n")

def add_contact(name, phone, email):
    name = name.lower()
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact has been added: \n"
          f"{contact_book[name]}")


def delete_contact(name):
    name = name.lower()
    if name in contact_book:
        del contact_book[name]
        print(f"{contact_book[name]} has been removed from your contacts")
    else:
        print("Contact cannot be found")


def search_contact(name):
    name = name.lower()
    if name in contact_book:
        print(contact_book[name])

    else:
        print("Contact cannot be found")


def update_contact(name, phone, email):
    name = name.lower()
    if name in contact_book:
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Email and phone has been updated:\n "
              f"{contact_book[name.title()]}")
    else:
        print("Contact does not exist")

def save_contact():
    with open('contacts.json', 'w') as f:
        json.dump(contact_book, f)

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def main():

    #Creates a dictionary of options to choose
    operation = {
        1: "Add Contact",
        2: "Delete Contact",
        3: "Search Contact",
        4: "Update Contact"
    }

    #Enters the while loop
    while True:
        print("Main Menu: ")

        for key, value in operation.items():
            print(f"[{key}] {value}")
        print("[0] Exit") # Print the option to exit

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter the correct number.")    #If the user enters a number that is not in the range of choice, Print Error Message
            continue

        if user_choice == 0:    #If Choice 0 exit Program
            print("Goodbye!")
            break

        elif user_choice in operation:
            print(f"\n{operation[user_choice]} selected.")

            if user_choice == 1: #Add Contact
                name = input("Enter the name of the contact: ")


                while True:
                    phone = input("Enter the phone number: ")
                    if len(phone) == 10 and phone.isdigit():    #Verifies if the phone number is within the proper length
                        break
                    else:
                        print("Please enter a valid 10-digit number.")  #If not repeat to ask for the phone number

                email = input("Enter the email address: ")
                add_contact(name, phone, email)



            elif user_choice == 2: #Delete Contact
                name = input("Enter the name of the contact: ")
                delete_contact(name)


            elif user_choice == 3: #Search Contact
                name = input("Enter the name of the contact: ")
                search_contact(name)


            elif user_choice == 4: #Update Contact
                name = input("Enter the name of the contact: ")

                if name in contact_book:
                    while True:
                        phone = input("Enter the phone number: ")
                        if len(phone) == 10 and phone.isdigit():
                            break
                        else:
                            print("Please enter a valid 10-digit number.")

                    email = input("Enter the email address: ")
                    update_contact(name, phone, email)

                else:
                    print("Contact does not exist")
        else:
            print("Error: Incorrect choice. Please select a number between from 0 to 4,")

if __name__ == "__main__":
    main()







