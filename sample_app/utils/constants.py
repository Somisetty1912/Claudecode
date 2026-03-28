"""
Centralized constants and magic numbers.
Consolidates all hardcoded values from the codebase.
"""

# Email configuration
SMTP_HOST = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "no-reply@example.com"

# Validation constraints
MIN_PASSWORD_LENGTH = 6
LARGE_ORDER_THRESHOLD = 1000  # Orders above this get discount
BULK_DISCOUNT_RATE = 0.10  # 10% discount

# Database files
USER_DB = "users.db"
ORDER_DB = "orders.db"

# Currency symbols
CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
}

# Default decimal places
CURRENCY_DECIMAL_PLACES = 2

# Role constants
ROLE_ADMIN = "admin"
ROLE_REGULAR = "regular"
ROLE_SUSPENDED = "suspended"
ROLE_ACTIVE = "active"

# Order status
ORDER_STATUS_ACTIVE = "active"
ORDER_STATUS_CANCELLED = "cancelled"

# Email subjects
EMAIL_SUBJECT_WELCOME = "Welcome"
EMAIL_SUBJECT_ORDER_CONFIRMED = "Order Confirmed"
EMAIL_SUBJECT_ORDER_CANCELLED = "Order Cancelled"

# Report headers
REPORT_HEADER_LINE_CHAR = "="
REPORT_HEADER_LINE_LENGTH = 20
