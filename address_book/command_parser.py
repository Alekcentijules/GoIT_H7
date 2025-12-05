"""Module for parsing user commands."""
from typing import Tuple, List

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Splits user input into a command and arguments.

    Args:
        user_input (str): String entered by the user.

    Returns:
        Tuple[str, List[str]]: (command in lowercase, list of arguments)

    Examples:
        >>> parse_input("add John 123")
        ('add', ['John', '123'])
        >>> parse_input("Hello")
        ('hello', [])
    """
    parts = user_input.strip().split()
    if not parts:
        return ()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args