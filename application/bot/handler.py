from typing import Optional
from application.bot.service import (add_birthday, add_contact, change_contact, find_phone, get_birthdays, 
                                     get_contact, get_all_contacts, delete_contact, parse_input, 
                                     read_contacts, remove_phone, remove_contacts, save_contacts, show_birthday)
from application.utilities.objects import AddressBook
from application.utilities.constants import Constants
from application.utilities.validations import input_error


OPERATIONS = {
    "add": add_contact,
    "add-birthday" : add_birthday,
    "all": get_all_contacts,
    "birthdays": get_birthdays,
    "change": change_contact,
    "close": save_contacts,
    "delete": delete_contact,
    "exit" : save_contacts,
    "find": get_contact,
    "hello": lambda *_: Constants.help_question,
    "help": lambda *_: Constants.help_text,
    "phone": find_phone,
    "read": read_contacts,
    "remove": remove_phone,
    "remove-contacts": remove_contacts,
    "show-birthday" : show_birthday
}

@input_error
def get_handler(user_input: str, contacts: AddressBook) -> Optional[str]:
    cmd, *args = parse_input(user_input)
    return OPERATIONS.get(cmd, lambda *_: Constants.invalid_command)(contacts, args)
