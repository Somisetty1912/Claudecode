"""
User management model.

REFACTORED for SOLID principles:
- Separation of Concerns: Database operations now use utils/database.py
- Single Responsibility: Removed email sending, reporting, and hashing
- Dependency Injection: Services injected as dependencies
- DRY: Validation consolidated in utils/validators.py
- ISP: Removed god class that violated multiple principles

CHANGES:
- DB operations use DatabaseConnection from utils/database.py
- Email sending delegated to EmailService
- Report generation delegated to ReportGenerator
- Validation delegated to validators module
- Type hints added throughout
"""

import hashlib
import logging
from typing import Optional, Tuple
from ..utils import validators, database, constants
from ..services.email_service import email_service
from ..services.report_service import report_generator

logger = logging.getLogger(__name__)


class UserManager:
    """
    Refactored user manager with separation of concerns.

    Responsibilities:
    - Create, read, update, delete user records
    - Coordinate with email service for notifications
    - Coordinate with report service for reporting

    Dependencies:
    - DatabaseConnection: For database operations
    - EmailService: For sending emails
    - ReportGenerator: For generating reports
    """

    def __init__(self, db_connection: Optional[database.DatabaseConnection] = None):
        """
        Initialize UserManager.

        Args:
            db_connection: DatabaseConnection instance (default: uses global user_db)
        """
        self.db = db_connection or database.user_db

    def create_user(self, name: str, email: str, password: str, role: str) -> bool:
        """
        Create a new user.

        Args:
            name: User name
            email: User email
            password: User password
            role: User role

        Returns:
            True if user created successfully, False otherwise
        """
        # Validate inputs
        if not validators.validate_user_input(name, email, password):
            logger.warning(f"Invalid user input for {email}")
            return False

        # Hash password
        hashed = hashlib.sha256(password.encode()).hexdigest()

        try:
            # Insert user into database
            self.db.execute_and_commit(
                "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
                (name, email, hashed, role),
            )
            logger.info(f"User created: {email}")

            # Send welcome email
            email_service.send_welcome_email(name, email)

            return True
        except Exception as e:
            logger.error(f"Failed to create user {email}: {e}")
            return False

    def get_user(self, user_id: int) -> Optional[Tuple]:
        """
        Get user by ID.

        Args:
            user_id: User ID

        Returns:
            User tuple or None if not found
        """
        if not validators.validate_user_id(user_id):
            return None

        try:
            return self.db.fetch_one(
                "SELECT * FROM users WHERE id = ?",
                (user_id,),
            )
        except Exception as e:
            logger.error(f"Failed to get user {user_id}: {e}")
            return None

    def get_all_users(self) -> list:
        """
        Get all users.

        Returns:
            List of user tuples
        """
        try:
            return self.db.fetch_all("SELECT * FROM users")
        except Exception as e:
            logger.error(f"Failed to get all users: {e}")
            return []

    def update_user(
        self,
        user_id: int,
        name: str,
        email: str,
        role: str,
    ) -> bool:
        """
        Update user information.

        Args:
            user_id: User ID
            name: New name
            email: New email
            role: New role

        Returns:
            True if update successful, False otherwise
        """
        # Validate inputs
        if not validators.validate_name(name):
            return False
        if not validators.validate_email(email):
            return False
        if not validators.validate_user_id(user_id):
            return False

        try:
            self.db.execute_and_commit(
                "UPDATE users SET name=?, email=?, role=? WHERE id=?",
                (name, email, role, user_id),
            )
            logger.info(f"User updated: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to update user {user_id}: {e}")
            return False

    def delete_user(self, user_id: int) -> bool:
        """
        Delete user by ID.

        Args:
            user_id: User ID

        Returns:
            True if delete successful, False otherwise
        """
        if not validators.validate_user_id(user_id):
            return False

        try:
            self.db.execute_and_commit(
                "DELETE FROM users WHERE id = ?",
                (user_id,),
            )
            logger.info(f"User deleted: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete user {user_id}: {e}")
            return False

    def generate_report(self) -> str:
        """
        Generate user report.

        Returns:
            Formatted user report string
        """
        try:
            users = self.get_all_users()
            return report_generator.generate_user_report(users)
        except Exception as e:
            logger.error(f"Failed to generate user report: {e}")
            return "Failed to generate report"

    def change_user_role(self, user_id: int, new_role: str) -> bool:
        """
        Change user role.

        REPLACEMENT for process_user() method.
        Follows Open/Closed Principle: extend by adding new role constants,
        not by modifying this method.

        Args:
            user_id: User ID
            new_role: New role

        Returns:
            True if role changed successfully, False otherwise
        """
        user = self.get_user(user_id)
        if not user:
            return False

        return self.update_user(user_id, user[0], user[1], new_role)


# Global user manager instance
user_manager = UserManager()
