import json

class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,name,phone):
        self.contacts.append(Contact(name,phone))

    def show(self):
        for contact in self.contacts:
            print(contact.name,contact.phone)

    def save(self):
        data = []
        for contact in self.contacts:
            data.append({"name":contact.name,"phone":contact.phone})
        with open("hi.json","w") as f:
            json.dump(data,f)

    def load(self):
        with open("hi.json","r") as f:
            data = json.load(f)
        for item in data:
            self.contacts.append(Contact(item["name"],item["phone"]))

s = AddressBook()
s.add_contact("Daniel","858-426-4200")
s.save()

s2 = AddressBook()
s2.load()
s2.show()