"""
Centralized formatting utilities.
Consolidates all formatting functions, eliminating DRY violations.
"""

from typing import Union, Dict, Tuple
from . import constants


def format_currency(amount: Union[int, float], currency_code: str = "USD") -> str:
    """
    Format amount as currency string.

    Args:
        amount: Amount to format
        currency_code: Currency code (USD, EUR, GBP)

    Returns:
        Formatted currency string

    Example:
        format_currency(100.5, "USD") -> "$100.50"
        format_currency(100.5, "EUR") -> "€100.50"
    """
    if currency_code not in constants.CURRENCY_SYMBOLS:
        raise ValueError(f"Unsupported currency code: {currency_code}")

    symbol = constants.CURRENCY_SYMBOLS[currency_code]
    return f"{symbol}{amount:.{constants.CURRENCY_DECIMAL_PLACES}f}"


def format_report_header(title: str, line_char: str = "=", line_length: int = 20) -> str:
    """
    Format report header with title and line separator.

    Args:
        title: Header title
        line_char: Character used for separator line
        line_length: Length of separator line

    Returns:
        Formatted header string

    Example:
        format_report_header("User Report") -> "User Report\n====================\n"
    """
    line = line_char * line_length
    return f"{title}\n{line}\n"


def format_report_line(key: str, value: str) -> str:
    """
    Format a single report line.

    Args:
        key: Label for the value
        value: Value to display

    Returns:
        Formatted report line

    Example:
        format_report_line("Name", "John Doe") -> "Name: John Doe\n"
    """
    return f"{key}: {value}\n"


def format_user_report_line(name: str, email: str, role: str) -> str:
    """
    Format user data for report display.

    Args:
        name: User name
        email: User email
        role: User role

    Returns:
        Formatted user report line

    Example:
        format_user_report_line("John", "john@example.com", "admin")
        -> "Name: John, Email: john@example.com, Role: admin\n"
    """
    return f"Name: {name}, Email: {email}, Role: {role}\n"


def format_order_report_line(order_id: int, total: float) -> str:
    """
    Format order data for report display.

    Args:
        order_id: Order ID
        total: Order total

    Returns:
        Formatted order report line

    Example:
        format_order_report_line(123, 99.99) -> "Order ID: 123, Total: 99.99\n"
    """
    return f"Order ID: {order_id}, Total: {total}\n"


def format_statistics(label: str, count: int) -> str:
    """
    Format statistics line.

    Args:
        label: Label for the statistic
        count: Count value

    Returns:
        Formatted statistics line

    Example:
        format_statistics("Admins", 5) -> "Admins: 5\n"
    """
    return f"{label}: {count}\n"
