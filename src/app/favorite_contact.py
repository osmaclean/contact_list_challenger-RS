def favoriteContact(contacts, i_contact):
    i_adjust = int(i_contact) - 1
    contacts[i_adjust]["favorite"] = True
    print("\nContact: '%s' has been marked as a favorite!" % i_adjust)
    return
