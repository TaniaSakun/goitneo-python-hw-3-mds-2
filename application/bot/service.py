from application.utilities.objects import AddressBook, Record
from application.utilities.constants import Constants
from datetime import datetime, timedelta, date

def parse_input(user_input: str) -> list[str]:
    cmd, *args = user_input.split()
    return [cmd.strip().lower(), *args]

def print_birthdays(birthday_by_day):
    result = ''
    for weekday, contacts in birthday_by_day.items():
        result += (f"{weekday}: {', '.join(contacts)}\n")
    
    return result
    
def add_contact(contacts: AddressBook, args: list[str]) -> str:
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_contact(record)
        
    return Constants.contact_added.format(name)

def add_birthday(contacts: AddressBook, args: list[str]) -> str:
    name, birthday = args
    record = contacts.find_record(name)
    record.add_birthday(birthday)
    
    return Constants.birthday_added.format(name)

def change_contact(contacts: AddressBook, args: list[str]) -> str:
    name, old_phone, new_phone = args
    record = contacts.find_record(name)
    
    if(record):
        record.edit_phone(old_phone, new_phone)
        return Constants.contact_changed.format(name)
    else:
        raise KeyError

def delete_contact(contacts: AddressBook, args: list[str]) -> str:
    contacts.delete_record(args[0])  
    return Constants.contact_deleted.format(args[0])

def find_phone(contacts: AddressBook, *args: list[str]) -> str:
    name = args
    record = contacts.find_record(name)
    return record.find_phone(name)

def get_all_contacts(contacts: AddressBook, *args: list[str]) -> str:
    if not contacts:
        return Constants.no_contacts_text
    return str(contacts)  

def get_birthdays(contacts: AddressBook, *args: list[str]) -> str:
    today = datetime.today().date()
    birthdays_by_day: dict[str, list[str]] = {}
    
    for contact in contacts.data.values():
        if contact.birthday:
            day, month, year = map(int, contact.birthday.value.split("."))
            birthday = date(year=year, month=month, day=day)
            birthday_this_year = birthday.replace(year=today.year)

            if today < birthday_this_year and birthday_this_year <= today + timedelta(days=7):
                weekday_name = birthday_this_year.strftime("%A")
                if weekday_name not in birthdays_by_day:
                    birthdays_by_day[weekday_name] = [str(contact)]
                    continue
            birthdays_by_day[weekday_name].append(str(contact))
    
    return print_birthdays(birthdays_by_day) 
 
def get_contact(contacts: AddressBook, args: list[str]) -> str:
    return contacts.find_record(args[0])

def read_contacts(contacts: AddressBook, args: list[str]) -> str:
    return contacts.read_from_file() 

def remove_contacts(contacts: AddressBook, args: list[str]) -> str:
    contacts.clear
    return Constants.contacts_removed
    
def remove_phone(contacts: AddressBook, args: list[str]) -> str:
    name, phone = args
    record = contacts.find_record(name)
    
    if not record:
        raise KeyError
    if record.remove_phone(phone):
        return Constants.phone_number_removed.format(phone, name)  
    else:
        return Constants.phone_number_not_exist.format(phone, name) 
     
def save_contacts(contacts: AddressBook, args: list[str]) -> str: 
    contacts.save_to_file()
        
def show_birthday(contacts: AddressBook, args: list[str]) -> str: 
    record = contacts.find_record(args[0]) 
    if record:
        if hasattr(record.birthday, "value"):
            return record.birthday.value
        else: 
            return Constants.birthday_not_exist.format(args[0])
    else:
        raise KeyError()

        
