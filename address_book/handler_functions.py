"""Module with command handlers for the assistant bot."""
from .book_tools import Record, AddressBook
from .utils import input_error

@input_error
def hello(args: list, address_book: AddressBook) -> str: 
    """Handles the 'hello' command — greets the user."""
    return 'How can I help you?'

@input_error
def add_contact(args: list, address_book: AddressBook) -> str:
        """Handles the 'add' command — adds a new contact or phone to an existing one."""
        name = args[0]
        phone = args[1]
        record = address_book.find(name)
        if record is None:
            record = Record(name)
            address_book.add_record(record)
            message = 'Contact added.'
        else:
            message = 'Contact update.'
        record.add_phone(phone)
        return message

@input_error
def change(args: list, address_book: AddressBook) -> str:
    """Handles the 'change' command — updates an existing contact."""
    if len(args) != 3:
        return 'Enter name, old phone and new phone.'
    name, old_phone, new_phone, *_ = args
    record = address_book.find(name)
    record.edit_phone(old_phone, new_phone)
    return 'Contact updated.'

@input_error
def phone(args: list, address_book: AddressBook) -> str:
    """Handles the 'phone' command — shows the phone number by name."""
    name = args[0]
    record = address_book.find(name)
    phones = "; ".join(p.value for p in record.phones)
    return f"{name}: {phones}"

@input_error
def add_bday(args: list, address_book: AddressBook):
    """Handles the 'phone' command — adds a new birthday to contact."""
    name, birthday, *_ = args
    record = address_book.find(name)
    record.add_birthday(birthday)
    return 'Birthday added.'

@input_error
def show_bday(args: list, address_book: AddressBook):
    """Handles the 'phone' command — shows the birthday by name."""
    name = args[0]
    record = address_book.find(name)
    if not record.birthday:
        return f"{name} has no birthday saved."
    return f"{name}'s birthday: {record.birthday}"

@input_error
def bdays(args: list, address_book: AddressBook):
    """Handles the 'birthdays' command — shows upcoming birthdays in next 7 days."""
    birthdays = address_book.get_upcoming_birthdays()
    if not birthdays:
        return 'There are no birthdays in the next 7 days.'
    persons = []
    for person in birthdays:
        persons.append(f"Congratulate {person['name']} — {person['birthday']}")
    return '\n'.join(persons)

@input_error
def all(args: list, address_book: AddressBook) -> str:
    """Handles the 'all' command — displays all saved contacts."""
    if not address_book.data:
        return 'No contacts saved.'
    return "\n".join(str(record) for record in address_book.data.values())

@input_error
def goodbye(args: list, address_book: AddressBook) -> str:
    """Handles the 'close' and 'exit' commands — says goodbye."""
    return 'Good bye!'

# Command dictionary: command → handler
COMMANDS = {
    'hello': hello,
    'add': add_contact,
    'change': change,
    'phone': phone,
    'add-birthday': add_bday,
    'show-birthday': show_bday,
    'birthdays': bdays,
    'all': all,
    'close': goodbye,
    'exit': goodbye
}