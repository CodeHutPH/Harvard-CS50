# Phonebook dictionary to store contact information

# Initializes an empty dictionary called phonebook to store contact information (names and numbers).
phonebook = {}

#Define SPACE ----------------------------------------------------------------------------------------------------------------------------------------- 
def space():
    """Adds BREAK LINE"""
    print("")
space()

# Defines a function named CREATE that takes two parameters: name (contact's name) and number (contact's number).
def create(name, number):
    """Creates or ADD a new contact to the phonebook""" #docstring - purpose of the function
    phonebook[name] = number #New Entry - Name is the KEY =and number is the VALUE.
    print(f"{name} was added successfully.") #Success Message

create("Francis", "123-456-7890") #TEST
create("Nico", "123-456-7890") #TEST
create("Abdon", "123-456-7890") #TEST

# Defines a function named READ with no parameters. This function is responsible for displaying all contacts in the phonebook.
def read():
    """Reads or VIEW all contacts in the phonebook""" #docstring - purpose of the function
    if phonebook: #if there's a value, PRINT all. // "if len(phonebook) > 0" // if TRUE
        space() #----------------------------------------------------------------------------------------------------------------------------------------
        print("List of Contacts:") #Header / Label
        for name, number in phonebook.items(): #Loop that iterates over each key-value pair in the phonebook dictionary. Unpacks each pair into variables NAME and NUMBER.
             print(f"{name}: {number}") #Print line is executed for each contact in the phonebook.
    else: #if there's NO VALUE // <= 0 // FALSE
        print("List of contacts is empty.") #Print Empty

read() #TEST

space() #DELETE----------------------------------------------------------------------------------------------------------------------------------------

#Defines a function SEARCH that takes a single parameter name, representing the contact name to be searched.
def search(name):
    """Search a specific contact in the phonebook through their name""" #docstring - purpose of the function
    if name in phonebook: #Checks if the provided name is present in the phonebook dictionary. / TRUE block
        print(f"Contact found for {name}: {phonebook[name]}") #Prints a message indicating that the contact was found, along with their name and phone number.
    else: #If there's no record of the name / FALSE block
        print(f"Contact not found for {name} in this phonebook.") #Print not found.

search("Francis") #TEST
search("Nico") #TEST
search("Yutuc") #TEST
search("Abdon") #TEST

space() #DELETE----------------------------------------------------------------------------------------------------------------------------------------

#MAIN PROGRAM LOOP - Adds Flexibility and Modularity - ABOVE CODE FOR GUIDE
while True: #Start the forever loop
    print("\nPhonebook Menu: ") #MENU Header
    print("1. ADD contact")     #CREATE a new contact
    print("2. VIEW contacts")   #VIEW all contacts
    print("3. SEARCH contact")  #SEARCH a specific contact
    print("4. QUIT")            #BREAK the program.

    #This line takes user input to determine their choice. The input() function prompts the user to enter a choice, and the entered value is stored in the variable choice.
    choice = input("\nEnter your choice (1-4): ") 

    if choice == "1": #CREATE
        name = input("Enter contact's name: ")      #PROMPT for NAME variable
        number = input("Enter contact's number: ")  #PROMPT for NUMBER variable
        create(name,number)                         #Function with arguments (name,number)
    
    elif choice == "2": #READ
        read()                                      #VIEW ALL CONTACTS

    elif choice == "3": #SEARCH
        name = input("Enter the contact name to search: ")  #PROMPT for NAME inside the phonebook.
        search(name)                                         #Function with argument (name)

    elif choice == "4": #BREAK
        print("Closing the phonebook program. Thank you for using! >.<")    #Print close the program
        break                                                               #ENDS the forever loop.

    else: #FALSE
        print("Invalid Choice. Pick 1-4 only.")                             #BACK TO MAIN LOOP IF INVALID


