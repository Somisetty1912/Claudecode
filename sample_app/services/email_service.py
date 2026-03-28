"""
Centralized email service.
Consolidates email sending logic from user.py and order.py.
Eliminates 3 duplicated email blocks.
"""

import smtplib
import logging
from typing import Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..utils import constants

logger = logging.getLogger(__name__)


class EmailService:
    """Centralized email sending service."""

    def __init__(
        self,
        smtp_host: str = constants.SMTP_HOST,
        smtp_port: int = constants.SMTP_PORT,
        sender_email: str = constants.SENDER_EMAIL,
    ):
        """
        Initialize email service.

        Args:
            smtp_host: SMTP server hostname
            smtp_port: SMTP server port
            sender_email: Sender email address
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.sender_email = sender_email

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> bool:
        """
        Send email to recipient.

        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body text

        Returns:
            True if email sent successfully, False otherwise
        """
        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(self.sender_email, recipient, message)
            server.quit()
            logger.info(f"Email sent to {recipient}: {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            return False

    def send_welcome_email(self, name: str, recipient: str) -> bool:
        """
        Send welcome email to new user.

        Args:
            name: User name
            recipient: Recipient email address

        Returns:
            True if email sent successfully, False otherwise
        """
        subject = constants.EMAIL_SUBJECT_WELCOME
        body = f"Hi {name}, welcome!"
        return self.send_email(recipient, subject, body)

    def send_order_confirmation_email(self, order_id: int, recipient: str) -> bool:
        """
        Send order confirmation email.

        Args:
            order_id: Order ID
            recipient: Recipient email address

        Returns:
            True if email sent successfully, False otherwise
        """
        subject = constants.EMAIL_SUBJECT_ORDER_CONFIRMED
        body = f"Order {order_id} placed!"
        return self.send_email(recipient, subject, body)

    def send_order_cancellation_email(
        self,
        order_id: int,
        reason: str,
        recipient: str,
    ) -> bool:
        """
        Send order cancellation email.

        Args:
            order_id: Order ID
            reason: Cancellation reason
            recipient: Recipient email address

        Returns:
            True if email sent successfully, False otherwise
        """
        subject = constants.EMAIL_SUBJECT_ORDER_CANCELLED
        body = f"Order {order_id} cancelled: {reason}"
        return self.send_email(recipient, subject, body)


# Global email service instance
email_service = EmailService()
