"""Module with command handlers for the assistant bot."""

from .processor_functions import add_contact, change_contact, output_phone

def handler_hello(args: str, contacts: str) -> str: 
    """Handles the 'hello' command — greets the user."""
    return 'How can I help you?'

def handler_add(args: str, contacts: str) -> str:
    """Handles the 'add' command — adds a new contact."""
    return add_contact(args, contacts)

def handler_change(args: str, contacts: str) -> str:
    """Handles the 'change' command — updates an existing contact."""
    return change_contact(args, contacts)

def handler_phone(args: str, contacts: str) -> str:
    """Handles the 'phone' command — shows the phone number by name."""
    return output_phone(args, contacts)

def handler_add_birthday(args: str, contacts: str):
    return 

def handler_show_birthday(args: str, contacts: str):
    pass

def handler_birthdays(args: str, contacts: str):
    pass

def handler_all(args: str, contacts: str) -> str:
    """
    Handles the 'all' command — displays all saved contacts.

    Returns:
        str: List of contacts in format "Name: Phone" or message about empty list.
    """
    if not contacts:
        return 'No contacts saved.'
    return "\n".join(f"{name}: {contact}" for name, contact in contacts.items())

def handler_goodbye(args: str, contacts: str) -> str:
    """Handles the 'close' and 'exit' commands — says goodbye."""
    return 'Good bye!'

# Command dictionary: command → handler
COMMANDS = {
    'hello': handler_hello,
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone,
    'all': handler_all,
    'close': handler_goodbye,
    'exit': handler_goodbye
}