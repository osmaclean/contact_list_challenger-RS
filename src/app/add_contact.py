def addContact():
    contact = {}
    contact.update(name=input("What's your name? "))
    contact.update(phone_number=input("What's your phone number? "))
    contact.update(address=input("What's your address? "))
    contact.update(favorite=False)
    return contact
