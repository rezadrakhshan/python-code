import datetime


contacts = {}
counter = 1


def add_contact():
    global counter
    name = input("Please enter the name: ")
    last_name = input("Please enter the last name: ")
    age = int(input("Please enter the age: "))

    now = datetime.datetime.now()
    year = now.strftime("%y")
    month = now.strftime("%m")

    id = year + month + str(counter).zfill(2)
    counter += 1

    contacts[id] = {"name": name, "last_name": last_name, "age": age}
    print(f"Contact with ID {id} added.")


def edit_contact():
    id = input("Enter the ID of the contact to edit: ")
    if id in contacts:
        name = input("New name: ")
        last_name = input("New last name: ")
        age = int(input("New age: "))
        contacts[id] = {"name": name, "last_name": last_name, "age": age}
        print(f"Contact with ID {id} edited.")
    else:
        print("The entered ID does not exist.")


def remove_contact():
    id = input("Enter the ID of the contact to remove: ")
    if id in contacts:
        del contacts[id]
        print(f"Contact with ID {id} removed.")
    else:
        print("The entered ID does not exist.")


def search_contact():
    id = input("Enter the ID of the contact to search: ")
    if id in contacts:
        print(
            f"Contact Information:\nName: {contacts[id]['name']}\nLast Name: {contacts[id]['last_name']}\nAge: {contacts[id]['age']}"
        )
    else:
        print("No contact found with this ID.")


while True:
    print("Menu:")
    print("1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Exit")

    choice = int(input("Please enter the number of your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        edit_contact()
    elif choice == 3:
        remove_contact()
    elif choice == 4:
        search_contact()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
