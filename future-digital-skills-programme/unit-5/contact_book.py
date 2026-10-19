# Command-line Contact Book

# Initialize contacts list
contacts = []


def add_contact(contacts_list, name, phone, email):
    """Append a new contact dictionary to the contacts list if name is unique."""
    existing = search_contact(contacts_list, name)
    if existing is not None:
        return False

    contacts_list.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    return True


def search_contact(contacts_list, name):
    """Search contacts by name. Return the contact dict or None if not found."""
    name_lower = name.lower()
    for contact in contacts_list:
        if contact["name"].lower() == name_lower:
            return contact
    return None


def delete_contact(contacts_list, name):
    """Remove a contact by name. Return True if deleted, False if not found."""
    name_lower = name.lower()
    for i, contact in enumerate(contacts_list):
        if contact["name"].lower() == name_lower:
            del contacts_list[i]
            return True
    return False


def view_all(contacts_list):
    """Display all contacts in a formatted layout."""
    if not contacts_list:
        print("\nNo contacts found.\n")
        return

    print("\n" + "=" * 55)
    print(f"{'CONTACT BOOK':^55}")
    print("=" * 55)

    for idx, contact in enumerate(contacts_list, start=1):
        print(f"\nContact {idx}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")

    print("\n" + "=" * 55)


def run_contact_book():
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add")
        print("2. Search")
        print("3. Delete")
        print("4. View All")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()

            added = add_contact(contacts, name, phone, email)
            if added:
                print(f"\nContact '{name}' added successfully!")
            else:
                print(f"\nA contact with the name '{name}' already exists.")

        elif choice == "2":
            name = input("Enter the name to search: ").strip()
            found = search_contact(contacts, name)

            if found is None:
                print(f"\nNo contact found for '{name}'.")
            else:
                print("\nContact found:")
                print(f"Name : {found['name']}")
                print(f"Phone: {found['phone']}")
                print(f"Email: {found['email']}")

        elif choice == "3":
            name = input("Enter the name to delete: ").strip()
            deleted = delete_contact(contacts, name)

            if deleted:
                print(f"\nContact '{name}' deleted successfully!")
            else:
                print(f"\nNo contact found for '{name}'.")

        elif choice == "4":
            view_all(contacts)

        elif choice == "5":
            print("\nExiting Contact Book. Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    run_contact_book()