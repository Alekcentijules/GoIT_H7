"""
Assistant Bot — Address Book Package

The module implements a console assistant bot for managing contacts:
- adding/changing/deleting contacts
- storing phone numbers and birthdays
- searching for upcoming birthdays (with transfer to Monday)
"""

from .book_tools import Record, AddressBook
from .command_parser import parse_input
from .handler_functions import COMMANDS
from .utils import input_error