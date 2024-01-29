# Phonebook dictionary to store contact information
phonebook = {}

def space():
    """Adds BREAK LINE"""
    print("")
space()

def create(name, number):
    """Creates or ADD a new contact to the phonebook"""  
    phonebook[name] = number 
    print(f"{name} was added successfully.") 
create("Francis", "123-456-7890") #TEST

def read():
    """Reads or VIEW all contacts in the phonebook""" 
    if phonebook:
        space() 
        print("List of Contacts:") 
        for name, number in phonebook.items():
             print(f"{name}: {number}")
    else:
        print("List of contacts is empty.")
read() #TEST

space()

def search(name):
    """Search a specific contact in the phonebook through their name"""
    if name in phonebook:
        print(f"Contact found for {name}: {phonebook[name]}")
    else:
        print(f"Contact not found for {name} in this phonebook.")
search("Francis") #TEST
search("Nico") #TEST

space()

while True:
    print("\nPhonebook Menu: ") 
    print("1. ADD contact")     
    print("2. VIEW contacts")   
    print("3. SEARCH contact")  
    print("4. QUIT")            

    choice = input("\nEnter your choice (1-4): ") 
    if choice == "1":
        name = input("Enter contact's name: ")      
        number = input("Enter contact's number: ")  
        create(name,number)
    elif choice == "2":
        read()                                      
    elif choice == "3":
        name = input("Enter the contact name to search: ")  
        search(name)                                        
    elif choice == "4":
        print("Closing the phonebook program. Thank you for using! >.<")
        break                                                           
    else:
        print("Invalid Choice. Pick 1-4 only.")                             