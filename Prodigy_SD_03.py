import json

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

# Define the filename for storing contacts
contacts_filename = "contacts.json"

# Load existing contacts
contacts = load_contacts(contacts_filename)

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts_filename, contacts)
    print(f"Contact {name} added successfully!")

def view_contact():
    name = input("Enter the name of the contact you want to view: ")
    if name in contacts:
        contact_info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
    else:
        print(f"Contact {name} not found.")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        save_contacts(contacts_filename, contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts_filename, contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Select an option (1/2/3/4/5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")