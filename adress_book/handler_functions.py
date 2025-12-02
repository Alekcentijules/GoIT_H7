"""Module with command handlers for the assistant bot."""

from .book import Record, AddressBook

def handler_hello(args: list, book: AddressBook) -> str: 
    """Handles the 'hello' command — greets the user."""
    return 'How can I help you?'

def handler_add(args: list, book: AddressBook) -> str:
        """Handles the 'add' command — adds a new contact."""
        name, phone, *_ = args
        record = book.find(name)
        message = 'Contact update.'
        if record is None:
            record = Record(name)
            contacts.add_record(record)
            message = 'Contact added.'
        if phone:
            record.add_phone(phone)
        return message

def handler_change(args: list, book: AddressBook) -> str:
    """Handles the 'change' command — updates an existing contact."""
    return Record.edit_phone(args, contacts)

def handler_phone(args: list, book: AddressBook) -> str:
    """Handles the 'phone' command — shows the phone number by name."""
    return Record.find_phone(args, contacts)

def handler_add_birthday(args: list, book: AddressBook):
    return Record.add_birthday(args)

def handler_show_birthday(args: list, book: AddressBook):
    if not args:
        return 'Enter a name pleace.'
    name = args[0]
    record = AddressBook.find(name)
    if not record:
        return 'Contact not found.'
    if not record.birthday:
        return f"{name} has no birthday saved."
    return f"{name}'s birthday: {record.birthday}"

def handler_birthdays(args: list, book: AddressBook):
    birthdays = AddressBook.get_incoming_birthdays()
    if not birthdays:
        return 'There are no birthdays in the next 7 days.'
    persons = []
    for person in birthdays:
        persons.append(f"Congratulate {person['name']} — {person['birthday']}")
    return '\n'.join(persons)

def handler_all(args: list, book: AddressBook) -> str:
    """
    Handles the 'all' command — displays all saved contacts.

    Returns:
        str: List of contacts in format "Name: Phone" or message about empty list.
    """
    if not AddressBook:
        return 'No contacts saved.'
    return "\n".join(f"{name}: {contact}" for name, contact in contacts.items())

def handler_goodbye(args: list, book: AddressBook) -> str:
    """Handles the 'close' and 'exit' commands — says goodbye."""
    return 'Good bye!'

# Command dictionary: command → handler
COMMANDS = {
    'hello': handler_hello,
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone,
    'add_birthday': handler_add_birthday,
    'show_birthday': handler_show_birthday,
    'birthdays': handler_birthdays,
    'all': handler_all,
    'close': handler_goodbye,
    'exit': handler_goodbye
}