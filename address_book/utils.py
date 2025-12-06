"""
This decorator centralizes error handling logic, ensuring consistent
and user-friendly error messages throughout the application.
"""

from functools import wraps
from typing import Callable

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
        except (IndexError, IndexError):
            return "Not enough arguments."
        except KeyError:
            return "Contact not found."
        except AttributeError:
            return "Operation failed. Contact may not exist."
        except Exception as err:
            return f"Error: {err}"
    return inner