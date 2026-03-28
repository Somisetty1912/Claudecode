"""
Helper utilities and data processors.

REFACTORED: Validation and formatting functions moved to:
  - utils/validators.py (validate_email, validate_user_input, validate_order_input)
  - utils/formatters.py (format_currency and variants)

ISP VIOLATION RESOLVED: DataProcessor base class removed due to forced implementation
of unneeded methods. Replaced with single-purpose service classes:
  - services/report_service.py (ReportGenerator)
  - services/email_service.py (EmailService)
"""

from typing import List, Optional, Dict, Any

# Re-export consolidated validators and formatters for backward compatibility
from .validators import (
    validate_email,
    validate_user_input,
    validate_order_input,
)
from .formatters import format_currency


def format_currency_eur(amount: float) -> str:
    """
    DEPRECATED: Use formatters.format_currency(amount, 'EUR') instead.

    Format currency as EUR.
    """
    from .formatters import format_currency
    return format_currency(amount, "EUR")


def format_currency_gbp(amount: float) -> str:
    """
    DEPRECATED: Use formatters.format_currency(amount, 'GBP') instead.

    Format currency as GBP.
    """
    from .formatters import format_currency
    return format_currency(amount, "GBP")


# REMOVED: DataProcessor and UserDataProcessor classes
# REASON: ISP violation - forced implementation of unneeded methods
# REPLACEMENT: Use service-specific classes instead
#   - ReportGenerator (services/report_service.py)
#   - EmailService (services/email_service.py)
