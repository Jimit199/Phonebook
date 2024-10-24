contacts={}
print("Welcome to the Phonebook")
print("What do you want to do today?")
print("1.add")
print("2.remove")
print("3.update")
print("4.display")
print("5.exit")

def add():
    name=input("Enter your name:")
    number=int(input("Enter your number"))
    if name in contacts:
        print("Name already exists")
    else:
        contacts[name]=number
        print("Contact Saved")

def remove():
    name=input("Enter your name:")
    if name not in contacts:
        print("Contact already deleted")
    else:
        del contacts[name]
        print("Contact Deleted")
        
def update():
    
    if name in contacts:
        name=input("Enter your name:")
        number=int(input("Enter your number"))
        contacts[name]=number
        print("Contact updated")
    else:
        print("Contact not found")