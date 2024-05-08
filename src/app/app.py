from add_contact import addContact
from view_contact import viewContacts
from edit_contact import editContact

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
        case 3:
            print("\n---------------------------")
            viewContacts(contacts)
            i_contact = input("Write a contact number you want to edit: ")
            new_name_contact = input("Write a new contact name: ")
            new_phone_number_contact = input(
                "Write a contact number you want to edit: "
            )
            new_address_contact = input("Write a contact number you want to edit: ")
            editContact(
                contacts,
                i_contact,
                new_name_contact,
                new_phone_number_contact,
                new_address_contact,
            )
            print("\nEdit your contact")
            print("\n---------------------------")
        case 6:
            break
