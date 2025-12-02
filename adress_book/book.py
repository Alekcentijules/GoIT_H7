"""
Module for managing an address book with support for contacts, phones, and validation.
Uses OOP, inheritance, UserDict, and strict typing.
"""

from datetime import datetime, timedelta
from collections import UserDict
from functools import wraps
from typing import Optional, List, Callable

def input_error(func: callable) -> Callable:
    """
    Decorator for handling errors in commands.

    Args:
        func (Callable): Command handler.

    Returns:
        Callable: Wrapped function.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
        except Exception as err:
            return f"Error: {err}"
    return inner

class Field:
    """
    Base class for record fields.

    Attributes:
        value (str): Stored field value.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the field with the specified value.

        Args:
            value (str): Field value.
        """
        self.value = value

    def __str__(self) -> None:
        """Returns a string representation of the value."""
        return str(self.value)
    
class Name(Field):
    """
    Class for storing a contact name. Required field.

    Inherited from Field.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the contact name.

        Args:
            value (str): Contact name.
        """
        super().__init__(value)

class Phone(Field):
    """
    Class for storing phone numbers with validation.

    The number must contain exactly 10 digits.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a phone number with format validation.

        Args:
            value (str): Phone number.

        Raises:
            ValueError: If the length is not 10 or contains non-numeric characters.
        """
        if len(value) != 10:
            raise ValueError("The lenth of the telephon number must be 10 numbers.")
        if not value.isdigit():
            raise ValueError("Value must consist of numbers.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError('Invalid date format. Use DD.MM.YYYY')
        super().__init__(value)

    @property
    def date(self) -> datetime:
        return datetime.strptime(self.value, "%d.%m.%Y").date()
    
class Record:
    """
    Class for storing contact information.

    Contains name and list of phone numbers.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a contact with a name.

        Args:
            name (str): Contact name.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday = None
    
    @input_error
    def add_phone(self, phone: str) -> None:
        """
        Adds a phone number to a contact.

        Args:
            phone_str (str): Phone number as a string.

        Raises:
            ValueError: If the number does not pass validation.
        """
        self.phones.append(Phone(phone))
    
    @input_error
    def add_birthday(self, args: str):
        self.birthday = Birthday(args)

    @input_error
    def remove_phone(self, phone: str) -> None:
        """
        Removes all occurrences of the specified phone number.

        Args:
            phone (str): Phone number to remove.
        """
        find = self.find_phone(phone)
        self.phones.remove(find)

    @input_error
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Replaces the first old number found with the new one.

        Args:
            old_phone (str): Old phone number.
            new_phone (str): New phone number.

        Raises:
            ValueError: If the old number is not found or the new one is invalid.
        """
        if not any(p.value == old_phone for p in self.phones):
            raise ValueError("Old number not found.")
        
        self.remove_phone(old_phone)
        self.phones.append(Phone(new_phone))
        
    @input_error
    def find_phone(self, phone: str) -> Optional[Phone]:
        """
        Searches for a phone number in the contact list.

        Args:
            phone (str): Phone number to search for.

        Returns:
            Optional[Phone]: Phone object if found, otherwise None.

        Raises:
            ValueError: If the number does not match the format (10 digits).
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None
        
    def __str__(self) -> str:
        """Returns a human-readable representation of the contact."""
        return f"Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}, birthday: {self.birthday}" if self.birthday else f"Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    """
    Class for storing and managing contact records.

    Inherited from UserDict. Keys are names (str), values are Record objects.
    """

    @input_error
    def add_record(self, record: Record) -> None:
        """
        Adds an entry to the address book.

        Args:
            record (Record): Contact object.
        """
        self.data[record.name.value] = record

    @input_error
    def find(self, name: str) -> Optional[Record]:
        """
        Finds a contact by name.

        Args:
            name (str): Contact name.

        Returns:
            Optional[Record]: Record object or None if not found.
        """
        return self.data.get(name)

    @input_error
    def delete(self, name: str) -> None:
        """
        Deletes a contact by name.

        Args:
            name (str): Contact name.
        """
        if name in self.data:
            del self.data[name]
    
    @input_error
    def get_incoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []
        for name, record in self.data.items():
            if not record.birthday:
                continue
            birthday = record.birthday.date.replace(year=today.year)
            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)
            if today <= birthday <= today + timedelta(days=7):    
                if birthday.weekday() >= 5:
                    days_to_monday = 7 - birthday.weekday()
                    cong_day = birthday + timedelta(days=days_to_monday)
                else:
                    cong_day = birthday
                upcoming.append({
                    "name": name, "birthday": cong_day.strftime("%d.%m.%Y")
                })
        return "\n".join(
            f"{item['name']} — congratulate day: {item['birthday']}"
            for item in upcoming 
        )

    def __str__(self) -> str:
        """Returns a string representation of the entire book."""
        return "\n".join(str(record) for record in self.data.values())
    

# ————————————————————————
# Example of use (for testing)
# ————————————————————————      
if __name__ == "__main__":
    book = AddressBook()

    johny_record = Record('Johny')
    johny_record.add_phone('3939393939')
    johny_record.add_phone('6464646333')

    book.add_record(johny_record)

    jane_record = Record('Jane')
    jane_record.add_phone('4365464563')
    jane_record.add_phone('4365464563')
    book.add_record(jane_record)

    print(book)

    jane = book.find('Jane')
    jane.edit_phone('4365464563', '2828282828')

    print(jane)

    found_phone = jane.find_phone('2828282828')
    print(f"{jane.name}: {found_phone}")

    book.delete('John')
    print(book)

    jane_record.add_birthday("29.11.2005")
    print(jane_record.birthday)

    jane_record.birthday = Birthday("29.11.2005")
    print(jane_record)

    print(book.get_incoming_birthdays())