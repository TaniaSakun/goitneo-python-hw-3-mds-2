import re
from collections import UserDict
from datetime import datetime
import pickle
from application.utilities.constants import (Constants, InvalidBirthdayError, InvalidNameError, 
                                             InvalidPhoneError, InvalidPhoneLengthError)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return hasattr(other, "value") and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __ne__(self, other):
        return not hasattr(other, "value") or self.value != other.value

class Name(Field):
    def __init__(self, value):
        if not value:
            raise InvalidNameError()
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise InvalidBirthdayError()

class Phone(Field):
    def __init__(self, value):
        pattern = re.compile(r'^[0-9+-]+$')
        
        if len(value) != 10:
            raise InvalidPhoneLengthError()   
        elif not pattern.match(value):
            raise InvalidPhoneError()
        
        super().__init__(value)
    

class Record:
    def __init__(self, name):
        self.name : Name = Name(name)
        self.phones : set[Phone] = set()
        self.birthday : Birthday = None

    def add_birthday(self, value):
        self.birthday = Birthday(value)
        
    def add_phone(self, phone):
        self.phones.add(Phone(phone))
    
    def remove_phone(self, phone):
        return bool(self.phones.discard(Phone(phone)))

    def edit_phone(self, old_phone, new_phone):
        self.phones.discard(Phone(old_phone))
        self.phones.add(Phone(new_phone))
    
    def find_phone(self, name):
        search_phone = [phone for phone in self.phones if name in phone.value]
        
        if search_phone:
            return Constants.phone_number_found.format(search_phone, name)
        else:
            return Constants.phone_number_not_exist.format(search_phone, name)
        
    def __str__(self):
        return Constants.contact_info.format(self.name.value, '; '.join(p.value for p in self.phones), self.birthday)


class AddressBook(UserDict[Name, Record]):        
    def __str__(self):
        return "\n".join(str(contact) for contact in self.data.values())

    def add_contact(self, contact):
        name = contact.name
        phones = contact.phones
        contact = self.data.setdefault(name, contact)
        
        for phone in phones:
            contact.add_phone(phone.value)
    
    def find_record(self, name):
        contact = self.data.get(Name(name), None)
        
        if contact:
            return contact
        else: 
            raise KeyError
    
    def delete_record(self, name):
        del self.data[Name(name)]
        
    def save_to_file(self):
        filename = Constants.file_name 
        
        if self.data.values():
            with open(filename, 'wb') as file:
                pickle.dump(self.data, file)
            return Constants.address_book_saved
        else:
            return Constants.address_book_empty

    def read_from_file(self):
        filename = Constants.file_name 
        
        with open(filename, 'rb') as file:
            if self.data.values():
                self.data.update(pickle.load(file))
            else:
                self.data = pickle.load(file) 
                
        return Constants.address_book_opened