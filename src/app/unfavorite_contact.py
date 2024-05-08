def unfavoriteContact(contacts, i_contact):
    i_adjust = int(i_contact) - 1
    contacts[i_adjust]["favorite"] = False
    print("\nContact: '%s' has been unmarked as a favorite!" % i_adjust)
    return
