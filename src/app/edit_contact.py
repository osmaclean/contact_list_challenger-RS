def editContact(
    contacts,
    i_contact,
    new_name_contact,
    new_phone_number_contact,
    new_address_contact,
):
    i_adjust = int(i_contact) - 1
    if i_adjust >= 0 and i_adjust < len(contacts):
        contacts[i_adjust]["name"] = new_name_contact
        contacts[i_adjust]["phone_number"] = new_phone_number_contact
        contacts[i_adjust]["address"] = new_address_contact
        print(
            "\nContato: '%s' foi atualizada para: '%s - %s - %s'"
            % (
                i_adjust + 1,
                new_name_contact,
                new_phone_number_contact,
                new_address_contact,
            )
        )
    else:
        print("\nContact not found!")
    return
