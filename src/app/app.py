from add_contact import addContact
from view_contact import viewContacts

contacts = []
while True:
    print("\nWelcome to Manager Contact\n")
    print("\n1 → Add a new contact")
    print("2 → View all contacts")
    print("3 → Edit your contact")
    print("4 → Favorite your contact")
    print("5 → Remove your contact")
    print("6 → Exit the program")

    escolha = int(input("\nWrite a wish option: "))

    match escolha:
        case 1:
            print("\n---------------------------")
            print("\nAdd a new contact")
            contact = addContact()
            contacts.append(contact)
            print("\nAdded contact successfully!")
            print("\n---------------------------")
        case 2:
            print("\n---------------------------")
            print("\nView all contacts")
            viewContacts(contacts)
            print("\n---------------------------")
        case 6:
            break
