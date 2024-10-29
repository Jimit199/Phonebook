contacts={}
print("Welcome to the Phonebook")
print("What do you want to do today?")
print("1.add")
print("2.remove")
print("3.update")
print("4.display")
print("5.exit")

#This is add
def add():
    name=input("Enter your name:")
    number=int(input("Enter your number"))
    if name in contacts:
        print("Name already exists")
    else:
        contacts[name]=number
        print("Contact Saved")

#This is remove
def remove():
    name=input("Enter your name:")
    if name not in contacts:
        print("Contact already deleted")
    else:
        del contacts[name]
        print("Contact Deleted")

        #This is update
def update():
    name=input("Enter your name:")
    if name in contacts:
        name=input("Enter your name:")
        number=int(input("Enter your number"))
        contacts[name]=number
        print("Contact updated")
    else:
        print("Contact not found")
        
        #This is Display
def display():
    print("Contact")
    for i in contacts:
        print(i,":",contacts[i])
        print()
        
while True:
    choice = input("Enter your Choice")
    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        update()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Thank you for using the PhoneBoook, Hope you enjoyed!")
        break
    else: 
        print("Invalid Option")