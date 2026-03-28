"""
Centralized validation logic.
Consolidates all validation functions from user.py, helpers.py, and order.py.
"""

from typing import Optional
import re


def validate_email(email: str) -> bool:
    """
    Validate email format.

    Args:
        email: Email address to validate

    Returns:
        True if email contains @, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    return "@" in email


def validate_password(password: str, min_length: int = 6) -> bool:
    """
    Validate password strength.

    Args:
        password: Password to validate
        min_length: Minimum password length (default: 6)

    Returns:
        True if password meets requirements, False otherwise
    """
    if not password or not isinstance(password, str):
        return False
    return len(password) >= min_length


def validate_name(name: str) -> bool:
    """
    Validate user name.

    Args:
        name: Name to validate

    Returns:
        True if name is non-empty string, False otherwise
    """
    if not name or not isinstance(name, str):
        return False
    return len(name.strip()) > 0


def validate_user_input(name: str, email: str, password: str, min_password_length: int = 6) -> bool:
    """
    Comprehensive user input validation.

    Args:
        name: User name
        email: User email
        password: User password
        min_password_length: Minimum password length

    Returns:
        True if all validations pass, False otherwise
    """
    return (
        validate_name(name)
        and validate_email(email)
        and validate_password(password, min_password_length)
    )


def validate_customer_id(customer_id: Optional[int]) -> bool:
    """
    Validate customer ID.

    Args:
        customer_id: Customer ID to validate

    Returns:
        True if customer_id is valid, False otherwise
    """
    if not customer_id:
        return False
    return isinstance(customer_id, int) and customer_id > 0


def validate_items(items: Optional[list]) -> bool:
    """
    Validate order items.

    Args:
        items: List of items to validate

    Returns:
        True if items is non-empty list, False otherwise
    """
    if not items or not isinstance(items, list):
        return False
    return len(items) > 0


def validate_total(total: Optional[float]) -> bool:
    """
    Validate order total.

    Args:
        total: Total amount to validate

    Returns:
        True if total is positive number, False otherwise
    """
    if total is None:
        return False
    try:
        total_float = float(total)
        return total_float > 0
    except (ValueError, TypeError):
        return False


def validate_order_input(customer_id: Optional[int], items: Optional[list], total: Optional[float]) -> bool:
    """
    Comprehensive order input validation.

    Args:
        customer_id: Customer ID
        items: Order items
        total: Order total

    Returns:
        True if all validations pass, False otherwise
    """
    return (
        validate_customer_id(customer_id)
        and validate_items(items)
        and validate_total(total)
    )


def validate_user_id(user_id: Optional[int]) -> bool:
    """
    Validate user ID for database operations.

    Args:
        user_id: User ID to validate

    Returns:
        True if user_id is valid, False otherwise
    """
    if not user_id:
        return False
    return isinstance(user_id, int) and user_id > 0


def validate_order_id(order_id: Optional[int]) -> bool:
    """
    Validate order ID for database operations.

    Args:
        order_id: Order ID to validate

    Returns:
        True if order_id is valid, False otherwise
    """
    if not order_id:
        return False
    return isinstance(order_id, int) and order_id > 0
