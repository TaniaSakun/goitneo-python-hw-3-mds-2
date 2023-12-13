class Constants:
   #Command messages
    address_book_opened = "AddressBook was successfully opened."
    address_book_saved = "AddressBook was successfully saved."
    birthday_added = "Birthday for contact {0} added."
    contact_added = "Contact {0} added."
    contact_changed = "Contact {0} changed."
    contact_deleted = "Contact {0} deleted."
    contact_info = "Contact name: {0}, phones: {1}, birthday: {2}"
    contact_not_found = "Contact not found."
    contacts_removed = "Contacts were removed from AddressBook."
    enter_command = "Enter a command: "
    file_name = 'address_book.pkl'
    help_question = "How can I help you?"
    help_text = """
    These are common commands used in various situations:
    start commands
        hello       Starting command
    set commands 
        add         Adds a new contact with a phone number. Note: takes name and phone number as parameters
        add-        Adds a birthday for existing contact. Note: takes name and birthday in format DD.MM.YYYY 
        birthday    as parameters         
        change      Changes phone number for the concrete contact. Note: takes name and phone number as parameters
        delete      Deletes phone number for the concrete contact. Note: takes name as parameter
        remove      Removes the phone number from the concrete contact. Note: takes name and phone number as parameters
        remove-     Removes all contacts from the AddressBook
        contacts 
               
    get commands
        all         Gets list of all created contacts with phone numbers
        birthdays   Gets birthdays that will happen in the next week
        help        In case you need help with detailed commands names and descriptions
        read        Read the AddressBook that was stored from the latest session
        phone       Gets phone number of the concrete contact. Note: takes a name as a parameter
        show-       Gets birthday of the concrete contact. Note: takes a name as a parameter
        birthday
    
    end commands
        close       Ends the interaction and saves the contacts to the file
        exit        Ends the interaction and saves the contacts to the file
    """
    good_bye_message = "Good bye!"
    phone_number_removed = "Phone number {0} removed from the contact {1}"
    phone_number_found = "Phone number {0} found. It belongs to the contact {1}"
    task_bot = "Bot task"
    
    #Error messages
    address_book_empty = "There is no contacts in the AddressBook to save."
    birthday_not_exist = "There is no birthday for the contact {0} in the AddressBook."
    eof_error = "End-of-Line Error."
    file_not_found = "The file you try to open is not found"
    invalid_command = "Invalid command."
    invalid_birthday = "Invalid birthday format. It should have the follovinf format: 'DD.MM.YYYY'"
    invalid_input = "Invalid command. Try again."
    invalid_name = "Invalid name for the Contact"
    invalid_parameters = "Give me name and phone please."
    phone_number_length = "Phone number must be 10 digits long."
    phone_number_not_exist = "There is no phone number {0} for the contact {1} in the AddressBook."
    phone_number_value = "Phone number must have only digits and '+' or '-' symbols."
    no_contacts_text = """Contacts have not been added yet. To add a contact, please enter the following command: 
    'add contactName phone', where contactName is the name of contact, and phone is a contact phone number."""
    contact_not_exist = "Contact do not exist."
    
#Custom exceptions  
class InvalidBirthdayError(Exception):
    ...
    
class InvalidNameError(Exception): 
    ...
    
class InvalidPhoneError(Exception):
    ...
    
class InvalidPhoneLengthError(Exception):
    ...