# ================================
# CONTACT BOOK APPLICATION
# ================================
# This program allows the user to:
# 1. Add contacts
# 2. View contacts
# 3. Search contacts
# 4. Update contacts
# 5. Delete contacts
# 6. Exit

contacts = []  # Empty list to store contacts

def show_menu():
    """Display the menu options to the user"""
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Add new contact
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully!")

    elif choice == "2":
        # View all contacts
        if not contacts:
            print("No contacts found!")
        else:
            for c in contacts:
                print(c["name"], "-", c["phone"])

    elif choice == "3":
        # Search contact
        search = input("Enter name or phone: ")
        found = [c for c in contacts if c["name"] == search or c["phone"] == search]
        if found:
            for c in found:
                print(c)
        else:
            print("No contact found!")

    elif choice == "4":
        # Update contact
        name = input("Enter name to update: ")
        for c in contacts:
            if c["name"] == name:
                c["phone"] = input("New Phone: ")
                c["email"] = input("New Email: ")
                c["address"] = input("New Address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found!")

    elif choice == "5":
        # Delete contact
        name = input("Enter name to delete: ")
        contacts = [c for c in contacts if c["name"] != name]
        print("Contact deleted!")

    elif choice == "6":
        # Exit program
        print("Goodbye! Exiting Contact Book...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")