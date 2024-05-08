def removeContact(contacts):
    for contact in contacts:
        if contact["favorite"]:
            contacts.remove(contact)
    print("\nFavorite contacts successfully removed!")
    return
