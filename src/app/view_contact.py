def viewContacts(contacts):
    print("\nContact list:\n")
    for i, contact in enumerate(contacts, start=1):
        favorite = "✓" if contact["favorite"] == True else " "
        name = contact["name"]
        phone_number = contact["phone_number"]
        address = contact["address"]
        print("%s → [%s] %s - %s - %s" % (i, favorite, name, phone_number, address))
    return
