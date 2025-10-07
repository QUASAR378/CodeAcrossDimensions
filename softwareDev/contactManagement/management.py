import json
import os

CONTACTS_FILE = "contacts.json"

# ---------- Utility Functions ----------

def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    """Display all contacts neatly."""
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    print("\n📇 Contact List:")
    print("-" * 40)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print("-" * 40)

# ---------- CRUD Operations ----------

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"\n✅ Contact '{name}' added successfully.\n")

def edit_contact(contacts):
    """Edit an existing contact."""
    display_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            print("❌ Invalid contact number.\n")
            return
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    contact = contacts[index]
    print(f"\nEditing contact: {contact['name']}")
    contact["name"] = input(f"New name [{contact['name']}]: ") or contact["name"]
    contact["phone"] = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
    contact["email"] = input(f"New email [{contact['email']}]: ") or contact["email"]

    save_contacts(contacts)
    print(f"\n✏️ Contact '{contact['name']}' updated successfully.\n")

def delete_contact(contacts):
    """Delete a contact."""
    display_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("❌ Invalid contact number.\n")
            return
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    deleted = contacts.pop(index)
    save_contacts(contacts)
    print(f"\n🗑️ Contact '{deleted['name']}' deleted successfully.\n")

# ---------- Main Program ----------

def main():
    contacts = load_contacts()

    while True:
        print("""
========= CONTACT MANAGER =========
1. View Contacts
2. Add Contact
3. Edit Contact
4. Delete Contact
5. Exit
===================================
""")
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\n👋 Goodbye! Contacts saved.\n")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
