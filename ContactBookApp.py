contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contacts')
    print('7. Exit')

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        if name in contacts:
            print(f'Contact with name "{name}" already exists!')
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact '{name}' has been created successfully!")

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print("Contact not found!")

    elif choice == '3':
        name = input("Enter name to update contact: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact '{name}' has been updated successfully!")
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' has been deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == '5':
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
                found = True
        if not found:
            print("No contact found with that name.")

    elif choice == '6':
        print(f"Total contacts in your book: {len(contacts)}")

    elif choice == '7':
        print('Goodbye...')
        break

    else:
        print("Invalid input. Please enter a number between 1 and 7.")
